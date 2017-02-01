import os
import sys
import subprocess

start=0
length=10

if len(sys.argv) < 2:
	print("Please provide a video file name. Additionally you can include the second " +
		  "from the video that the GIF starts on and the GIF's length in seconds.")
	exit()

video = sys.argv[1]
gif_folder = 'GIFs/'
if not os.path.exists(gif_folder): os.mkdir(gif_folder)
gif_file = gif_folder + os.path.splitext(os.path.basename(video))[0] + '.gif'



# Assigns default values from the start of the file if none given at command line
if len(sys.argv) > 2: start_time = sys.argv[2]
else: start_time = start

if len(sys.argv) > 3: duration = sys.argv[3]
else: duration = length

filters = 'fps=15,scale=480:-2:flags=lanczos'
palette = gif_folder + 'palette.png'

# the first run generates a global palette of 256 colors that will be used for every frame

# the stats_mode option can be either stats_mode=diff or stats_mode=full
# stats_mode=full chooses colors that will optimize colors for the entire frame
# while stats_mode=diff optimizes colors to make the changes look good
subprocess.call('ffmpeg -v error -ss ' + str(start_time) + ' -t ' + str(duration) + ' -i ' + video +
				' -vf "' + filters + ',palettegen=stats_mode=diff" -y ' + palette, shell=True)

# the second run uses the color palette while making the GIF
subprocess.call('ffmpeg -v error  -ss ' + str(start_time) + ' -t ' + str(duration) + ' -i ' + video +
				' -i ' + palette + ' -lavfi "' + filters + '[x]; [x][1:v] paletteuse" -y ' +
				gif_file, shell=True)

os.remove(palette)
