# you-can-datamosh-on-Linux

It's a script that makes datamoshing with Python fun and easy.

Hello, friends. If you have Python 3 and ffmpeg installed you can datamosh.
This might work on an Apple Mac but I don't have one to test on so I don't know for sure.

What's a datamosh?

Here's an example made by someone who wasn't me!

https://vimeo.com/87545616

The mosh works out of the box but I left extensive notes in the program to help you use it and understand what's happening.

How to run the program after it's downloaded:

`  $ python3 do_the_mosh.py [video file name]`
  
The datamoshed video will be in a new directory: `moshed_videos/`

Good luck, friends!

#

Need videos to datamosh? Head over to Python's pip3 and install youtube-dl.

`  $ pip3 install youtube-dl     # you may need to use sudo depending on your system.`
  
Afterwards downloading youtube videos is as simple as:

`  $ youtube-dl --format 18 [youtube video url] -o youtube_video.mp4`

But wait, there's more: youtube-dl works with lots of other sites like vimeo and can grab most twitter videos.
To discover if a site is supported try:

`  $ youtube-dl --list-formats [website url]`
  
which will show a list of available formats for the video on the page.

NOTE: If youtube-dl fails to download youtube videos try it on another site before deciding youtube-dl is broken.
Sometimes youtube makes changes to its video player and it takes the youtube-dl team a few days to catch up.
