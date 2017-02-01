import os
import sys
import subprocess

start_gif = 0
end_gif = 10

fps = 15
gif_width = 480

if len(sys.argv) < 2:
	print("Please provide a video file name. Additionally you can include the start and end times " +
		  "from the video for the GIF to copy.")
	exit()

video = sys.argv[1]
gif_folder = 'GIFs/'
if not os.path.exists(gif_folder): os.mkdir(gif_folder)
gif_file = gif_folder + os.path.splitext(os.path.basename(video))[0] + '.gif'



# Assigns default values from the start of the file if none given at command line
if len(sys.argv) > 2: start_time = sys.argv[2]
else: start_time = start_gif


if len(sys.argv) > 3: duration = float(sys.argv[3]) - float(start_time)
else: duration = float(start_time) + float(end_gif)

filters = 'fps=' + str(fps) + ',scale=' + str(gif_width) + ':-2:flags=lanczos'
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
