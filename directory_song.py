#Will simply open the Geometry Dash song directory on file explorer for easy access.

from subprocess import Popen
from glob import glob
from os import chdir

def open(gd_song_path):
    chdir(gd_song_path)
    song_list = glob("*.mp3")

    Popen(f'explorer /select,"{gd_song_path}\{song_list[0]}"')

def main():
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    
    open(gd_song_path)


if __name__ == '__main__':
    main()