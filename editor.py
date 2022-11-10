from moviepy.editor import *
import os
from moviepy.video.fx.all import loop
from moviepy.video.fx.resize import resize

#os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/kedrovnick/Downloads/ffmpeg.exe"
movie_path = "/Users/kedrovnick/Downloads/"
clip = VideoFileClip(movie_path + "dancing.mp4")

newClip = loop(clip, duration=600);
newClip.write_videofile("newClip.mp4", fps=25, codec='libx264');
