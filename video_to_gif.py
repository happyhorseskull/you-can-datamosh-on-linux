import os
from argparse import ArgumentParser
import sys
import subprocess

def bail_on_notfile(path):
        '''Validator for file existence for use in argparsing'''
        if not os.path.isfile(path):
                raise ArgumentTypeError("Couldn't find {}. You might want to check the file name??".format(path))
        else:
                return path

def mkdir_p(path):
        '''Checks if output dir exists, creates if not, for use in argparsing'''
        if not os.path.exists(path): os.mkdir(path)
        return path

parser = ArgumentParser()
parser.add_argument('video', type = bail_on_notfile, help = 'Video to be GIFarrooed')
parser.add_argument('start_time', type=float, nargs = '?', default = 0.0, help='start time')
parser.add_argument('end_time', type=float, nargs = '?', default = 10.0, help='end time')

parser.add_argument('--gif_folder', default='GIFS', type=mkdir_p, help='Folder for gif')
parser.add_argument('--fps', default = 15, help='Frames per second')
parser.add_argument('--gif_width', default = 480, help='GIF width in pixels')

args = parser.parse_args()
locals().update(args.__dict__.items()) # still bad practice, still gonna do it, muah ha ha ha ha

gif_file = os.path.join(gif_folder, os.path.splitext(os.path.basename(video))[0] + '.gif')

duration = float(start_time) + float(end_time)

filters = 'fps=' + str(fps) + ',scale=' + str(gif_width) + ':-2:flags=lanczos'
palette = os.path.join(gif_folder, 'palette.png')

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
