#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

# make sure a video was included at command line
if len(sys.argv) < 2:
	print("Please include a video to be datamoshed.")
	exit()

if not os.path.isfile(sys.argv[1]):
	print("Couldn't find that video file. You might want to check the file name??")
	exit()
else:
	input_video = sys.argv[1]			# We're assuming you gave it a valid video file and not a .txt or whatever.
										# If you want file validation you'll have to write it yourself.

fn = os.path.splitext(os.path.basename(input_video))[0]
input_avi =  'datamoshing_input.avi'					# must be an AVI so i-frames can be located in binary file
output_avi = 'datamoshing_output.avi'
output_dir = 'moshed_videos/'
output_video = output_dir + 'moshed_' + fn + '.mp4'		# this ensures we won't over-write your original video

# variables
fps = 25								# The number of frames per second the initial video is converted to before moshing.
start_sec = 3.1							# Time the effect starts on the original footage's timeline. The output video can be much longer.
end_sec   = 6.8							# Time the effect ends on the original footage's timeline.
repeat_p_frames = 15					# If this is set to 0 the result will only contain i-frames. Possibly only a single i-frame.
output_length = 60						# In seconds. ffmpeg also accepts 00:01:00.000 format.
output_video_width_in_pixels = 480		# 480 is Twitter-friendly. Programs get real mad if a video is an odd number of pixels wide (or in height).


	##############################################################################################################
	##############################################################################################################
	##                                                                                                          ##
	##                                              A bit of explanation                                        ##
	##                                                                                                          ##
	##      Datamoshing is a time honored glitching technique discovered by a hero of another era               ##
	##      or perhaps a god. We'll never know who they were but they're probably really old right now so       ##
	##      say a prayer for them in your heart. Also consider donating your youthful blood to them so they     ##
	##      can live forever on Peter Thiel's seastead paradise which is totally a good idea and not the        ##
	##      crackpot idea of a sheltered, solipsistic man with access to billions of other people's dollars.    ##
	##                                                                                                          ##
	##      A common method of datamoshing uses Avidemux which tends to get crashy when you mess with the       ##
	##      internals of video files. If that seems your more likely route to datamosh glory there are lots     ##
	##      of good tutorials on the internet. Have fun, good luck, no I don't know which Avidemux version      ##
	##      you should use.                                                                                     ##
	##                                                                                                          ##
	##      What's happening in the code below is that first your video file is converted to AVI format         ##
	##      which is glitch friendly as it sort-of doesn't care if you delete frames from the middle            ##
	##      willy-nilly (mp4 gets real mad if you delete stuff in a video file).                                ##
	##                                                                                                          ##
	##      There are 2 types of frames that we're dealing with: i-frames and p-frames.                         ##
	##      I-frames (aka key frames) give a full frame's worth of information while p-frames are               ##
	##      used to calculate the difference from frame to frame and avoid storing lots of                      ##
	##      redundant frame information. A video can be entirely i-frames but the file size is much larger      ##
	##      than setting an i-frame every 10 or 20 frames and making the rest p-frames.                         ##
	##                                                                                                          ##
	##      The first i-frame is the only one that's required and after that we use p-frames                    ##
	##      to calculate from frame to frame. The encoding algorithm then makes inter-frame calculations        ##
	##      and sometimes interesting effects happen.                                                           ##
	##                                                                                                          ##
	##      Initially datamoshing was just deleting the extra i-frames maybe smooshing some p-frames            ##
	##      in from another video and seeing what you got. However the glitchers eventually grew bored of       ##
	##      this and discovered if they repeated p-frames that the calculations would cause a blooming          ##
	##      effect and the results were real rowdy. So that's what the repeat_p_frames variable does and        ##
	##      that's why "it sounds like a dying printer"-@ksheely. Because we're repeating p-frames the video    ##
	##      length may get much longer. At ((25fps - 1 i-frame)) * 15 or (24 * 15) a single second of           ##
	##      24 frames turns into 360 frames which is (360 frames / 25 fps) = 14.4 seconds.                      ##
	##                                                                                                          ##
	##      After we're done mucking around with i-frames and p-frames the results are fed to ffmpeg            ##
	##      which locks in the glitches and makes a twitter-ready video to share with your friends              ##
	##      After you share about 10 of these you'll either be better friends with them or they'll stop         ##
	##      acknowledging you and delete you from their social media lifestyle which will                       ##
	##      then open up slots for all your new good friends who enjoy datamoshing thus giving your peer group  ##
	##      a common bond and sense of purpose as you continue the journey of life together, forever.           ##
	##                                                                                                          ##
	##############################################################################################################
	##############################################################################################################


# make sure ffmpeg is installed
try:
	# pipe output to /dev/null so it doesn't muck up our beautiful command line
	null = open("/dev/null", "w")
	subprocess.Popen("ffmpeg", stdout=null, stderr=null)
	null.close()

except OSError:
	print("ffmpeg was not found. Please install it. Thanks.")
	exit()

# convert original file to avi
subprocess.call('ffmpeg -loglevel error -y -i ' + input_video +
				' -crf 0 -pix_fmt yuv420p -r ' + str(fps) +
				' -vf scale=' + str(output_video_width_in_pixels) + ':-1 ' +
				input_avi, shell=True)

in_file  = open(input_avi,  'rb')
out_file = open(output_avi, 'wb')

in_file = in_file.read()

# 30306463 (ASCII 00dc) signals the end of a frame
frames = in_file.split(bytes.fromhex('30306463'))

# 0001B0 signals the beginning of an i-frame. Additional info: 0001B6 signals a p-frame
iframe = bytes.fromhex('0001B0')

# We want at least one i-frame before the glitching starts
i_frame_yet = False

for index, frame in enumerate(frames):

	if  i_frame_yet == False or index < int(start_sec * fps) or index > int(end_sec * fps):

		# the split above removed the end of frame signal so we put it back in
		out_file.write(frame + bytes.fromhex('30306463'))

		# found an i-frame, let the glitching begin
		if frame[5:8] == iframe: i_frame_yet = True

	else:
		# if it's not an i-frame it's a p-frame
		if frame[5:8] != iframe:
			# this repeats the p-frame x times
			for i in range(repeat_p_frames):
				out_file.write(frame + bytes.fromhex('30306463'))

# make sure the output directory exists
if not os.path.exists(output_dir): os.mkdir(output_dir)

# Convert avi to mp4. If you want a different format try changing the output variable's file extension
# and commenting out the line below that starts with -crf. If that doesn't work you'll be making friends with ffmpeg's many, many options.
subprocess.call('ffmpeg -loglevel error -y -i ' + output_avi + ' ' +
				' -crf 18 -pix_fmt yuv420p -vcodec libx264 -acodec aac -r ' + str(fps) +
				' -t ' + str(output_length) + ' ' +
				output_video + ' # 2> /dev/null', shell=True)

# gets rid of the in-between files so they're not crudding up your system
os.remove(input_avi)
os.remove(output_avi)


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

# the code was adapted from https://github.com/amgadani/Datamosh-python/blob/master/standard.py by @amgadani
# which was adapted from https://github.com/grampajoe/Autodatamosh/blob/master/autodatamosh.pl by @joefriedl

# Here comes the disclaimer. Basically you can include this code in commercial or personal projects and you're welcome to edit the code.
# If it breaks anything it's not my fault and I don't have to help you fix the work computer you broke while glitching on company time.
# Also I'm not obligated to help you fix or change the code but if your request is reasonable I probably will.

############################################################################################################################################
############################################################################################################################################
##                                                                                                                                        ##
##      Copyright <2017-ish> <happyhorseskull enterprises, a totally real organization that wasn't made up to fill in a blank>            ##
##                                                                                                                                        ##
##      Permission is hereby granted, free of charge, to any person obtaining a copy of this                                              ##
##      software and associated documentation files (the "Software"), to deal in the Software                                             ##
##      without restriction, including without limitation the rights to use, copy, modify, merge,                                         ##
##      publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons                                        ##
##      to whom the Software is furnished to do so, subject to the following conditions:                                                  ##
##                                                                                                                                        ##
##      The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.    ##
##                                                                                                                                        ##
##      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES   ##
##      OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE   ##
##      LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR    ##
##      IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                                     ##
##                                                                                                                                        ##
############################################################################################################################################
############################################################################################################################################
