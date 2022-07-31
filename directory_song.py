#Will simply open the Geometry Dash song directory on file explorer for easy access.

from subprocess import Popen
from glob import glob
from os import chdir


def open_directory(gd_song_path):
    chdir(gd_song_path)
    song_list = glob("*")

    Popen(f'explorer /select,"{gd_song_path}\{song_list[0]}"')
