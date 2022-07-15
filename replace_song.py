import pafy
import os, glob
import subprocess
import sys
import shutil
from colorama import Fore
from rich.console import Console

console = Console()

#Variables:
gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
current_path = os.getcwd()
url = str(sys.argv[1])
song_id = str(sys.argv[2])

def Move_to_gd(filename):
    #Move the new mp3 file to the "Geomtry Dash" folder that contains all the related songs
    os.chdir(current_path)
    if filename + ".mp3" in glob.glob("*.mp3"):
        shutil.move(f"{filename}.mp3", gd_song_path)

        print("\n")
        console.print(f"MOVED YOUR SONG TO {gd_song_path}, AS: {filename}.mp3", style="bold green")
    else:
        print("\n")
        console.print(f"'{filename}.mp3' WAS NOT FOUND IN THE CURRENT DIRECTORY: {current_path}", style="bold red")

    

def Rename_existing(filename):
    #Renames the existing file at "gd_song_path"
    try:
        os.rename(f"{gd_song_path}\\{filename}.mp3", f"{gd_song_path}\\{filename}-original.mp3")

        print("\n")
        console.print(f"RENAMED THE ORIGINAL FILE AS: {filename}-original.mp3", style="bold green")
    except FileExistsError as e:
        print("\n")
        console.print(f"'{filename}-original.mp3' ALREADY EXISTS IN: {gd_song_path}.", style="bold red")

def Replace(filename):
    os.chdir(gd_song_path)
    if filename + ".mp3" in glob.glob("*.mp3"):
        Rename_existing(filename)
        
        Move_to_gd(filename)
    else:
        Move_to_gd(filename)

def Download():
    #Identify and donwload the song:
    video = pafy.new(url)

    print("\n")
    console.print(f"FOUND: {video.title}", style="bold green")

    audio = video.getbestaudio()
    os.chdir(current_path)
    audio.download()

    return video

def Convert_to_mp3(video):
    #Convert the song from webm to mp3 using ffmpeg
    subprocess.run([r"C:\FFMPEG\ffmpeg", "-i", f"{video.title}.webm", f"{song_id}.mp3"], shell=True)

    console.print(f"Converted {video.title}.webm to 'mp3'", style="bold green")


def main():
    video = Download()
    Convert_to_mp3(video)
    Replace(song_id)

    os.remove(video.title + ".webm")

if __name__ == '__main__':
    main()
