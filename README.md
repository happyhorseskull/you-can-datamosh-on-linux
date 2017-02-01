#
#### you-can-datamosh-on-Linux (and Apple Macintosh, see the notes at the bottom)
#

Hello, friends! If you have Python 3 and ffmpeg installed you can datamosh!

(If you're running this on an Apple Macintosh see the notes below.)

What's a datamosh?

Here's an example made by someone who wasn't me!

https://vimeo.com/87545616

The mosh works out of the box and produces videos ready for social media sites like Twitter but I left extensive notes in the code to help you modify settings and understand what's happening.

How to run the datamosh program:

`$ python3 do_the_mosh.py [video file name]`
  
The datamoshed video will be in a new directory: `moshed_videos/`

You can most easily contact me on twitter. I am @happyhorseskull there as well.

Good luck, friends!


#

Editing python files is really easy with a simple code editor like https://atom.io/

If your editing session gets wild and you're not sure how to fix the code you can always re-download it from this github page so fear not!

Here are the really important variables in `do_the_mosh.py` for changing the video it creates:

`start_sec = 3` Time the effect starts on the original video's timeline. The final video can be much longer.

`end_sec = 6` Time the effect ends on the original video's timeline.

`output_length = 60` How long the final video will be in seconds

`repeat_p_frames = 15` How many times a p-frame is repeated during the datamosh


#
##### ffmpeg

If you don't have ffmpeg already you can find instructions for getting it here: http://ffmpeg.org/download.html

ffmpeg makes it super easy to trim a video:

`$ ffmpeg -v error -i [original video file name].mp4 -ss 30 -t 10 [new video file name].mp4`

`-ss` says to start copying the original video at 0:30 seconds and `-t` is how many seconds long the video will be which means the new shorter video is a copy of 0:30 through 0:40 of the original video.


#
##### GIF? GIF! with video_to_gif.py

Okay so MP4 files are fun and good but what about GIFs? That is not a problem with ffmpeg

`$ ffmpeg -v error -i [video file name].mp4 [gif file name].gif`

However the GIFs from that are kinda not that great so I adapted the information from http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html and made `video_to_gif.py` for your high-quality GIF convenience! The command to use it is:

`$ python3 video_to_gif.py [video file name]`

Your new GIF will be in the `GIFs` folder as `[original video file name].gif`

The current settings in `video_to_gif.py` will copy the first 10 seconds of the video to the GIF. But it it easy to change that. You can either:

- run the file from the command line and specify the start time and end time:
`$ python3 video_to_gif.py [video file name] 10 20`
which will start at the 10th second and end on the 20th second.

or:
- you can edit `video_to_gif.py` and change the `start_gif` and `end_gif` variables to be whichever default values you prefer.

GIFs can become suprisingly large files. If you need to make a GIF file size smaller you can make it shorter or you can edit some variables in `video_to_gif.py`

`fps` is frames per second. A lower `fps` will create smaller files.

`gif_width` sets how wide the GIF is. The height will scale to match. A narrower width GIF will have a smaller file size.

Warning: `video_to_gif.py` will overwrite previous GIFs made from the same video file if you leave them in the GIFs directory.


#
##### pip3

Need videos to datamosh? Head over to Python's pip3 and install youtube-dl.

`$ pip3 install youtube-dl     # you may need to use sudo depending on your system.`
  
Afterwards downloading youtube videos is as simple as:

`$ youtube-dl --format 18 [youtube video url] -o youtube_video.mp4`

But wait, there's more: youtube-dl works with lots of other sites like vimeo and can grab most twitter videos.
To discover if a site is supported try:

`$ youtube-dl --list-formats [website url]`
  
which will show a list of available formats for the video on the page.

NOTE: If youtube-dl fails to download youtube videos try it on another site before deciding youtube-dl is broken.
Sometimes youtube makes changes to its video player and it takes the youtube-dl team a few days to catch up.

The pip3 update command will get the most up-to-date version:

`$ pip3 install update youtube-dl`


#
##### Apple Macintosh notes

If your machine does not have Python 3 installed you can get it from Homebrew.

This page will help you with that http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx

Open `do_the_mosh.py` in a text editor like http://macromates.com/ and remove the first line `#!/usr/bin/python3` then you can run it with:

`$ py3 do_the_mosh.py`

(If that doesn't work you may need to find where Py3 was installed with `$ which py3` or maybe `$ which python3`)

Also you'll probably want to get ffmpeg from Homebrew if you don't have it already. Helpful instructions are available here https://trac.ffmpeg.org/wiki/CompilationGuide/MacOSX#ffmpegthroughHomebrew

Good luck!
