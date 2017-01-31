# you-can-datamosh-on-Linux (and Apple Macintosh, see the notes at the bottom)

Hello, friends! If you have Python 3 and ffmpeg installed you can datamosh!

(If you're running this on an Apple Macintosh see the notes below.)

What's a datamosh?

Here's an example made by someone who wasn't me!

https://vimeo.com/87545616

The mosh works out of the box and produces videos ready for social media sites like Twitter but I left extensive notes in the code to help you modify settings and understand what's happening.

How to run the program after it's downloaded:

`$ python3 do_the_mosh.py [video file name]`
  
The datamoshed video will be in a new directory: `moshed_videos/`

You can most easily reach me on twitter. I am @happyhorseskull there as well.

Good luck, friends!

#

Editing `do_the_mosh.py` is really easy with a simple code editor like https://atom.io/

If your editing session gets wild and you're not sure how to fix the code you can always re-download it from here so fear not!

#

GIF? GIF!

Okay so mp4 files are fun and good but what about GIFs? That is not a problem with ffmpeg.

`ffmpeg -v error -i moshed_videos/moshed_[moshed video file name].mp4 [file name].gif`

Note: the default settings in `do_the_mosh.py` produce 60 second videos which is a bit much for a GIF and you'll want to edit the video output settings down to say 10 seconds or less so when you convert the mp4 you aren't getting 84 MB GIF files that cause many GIF players give up and quit.


--ADVANCED GIF LEARNING--

The results will be okay but if you want to improve the output you'll find ideas here: http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html

#

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
Apple Macintosh notes

If your machine does not have Python 3 installed you can get it from Homebrew.

This page will help you with that http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx

Open `do_the_mosh.py` in a text editor like http://macromates.com/ and remove the first line `#!/usr/bin/python3` then you can run it with:

`$ py3 do_the_mosh.py`

(If that doesn't work you may need to find where Py3 was installed with `$ which py3` or maybe `$ which python3`)

Also you'll probably want to get ffmpeg from Homebrew if you don't have it already. Helpful instructions are available here https://trac.ffmpeg.org/wiki/CompilationGuide/MacOSX#ffmpegthroughHomebrew

Good luck!
