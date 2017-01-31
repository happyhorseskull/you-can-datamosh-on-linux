# you-can-datamosh

It's a script that makes datamoshing with Python fun and easy.

Hello, friends. If you have Python 3 and ffmpeg installed you can datamosh.
I've only tested this on Linux so good luck chuck if you're using something else.

What's a datamosh?

Here's an example made by someone who wasn't me!

https://vimeo.com/87545616

The mosh works out of the box but I left extensive notes in program to help you use it.

Good luck, friends!

__________________________________________________________________________________________

Need videos to datamosh? Head over to Python's pip3 and install youtube-dl.
After that downloading youtube videos is as simple as:

  $ youtube-dl -f 18 [youtube video url] -o youtube_video.mp4

But wait, there's more: youtube-dl works with lots of other sites like vimeo and can grab most twitter videos.
To discover if a site is supported try:

  $ youtube-dl -F [website url]
  
which show a list of available formats.
