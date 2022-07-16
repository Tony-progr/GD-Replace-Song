import pafy #Used for finging and dowloading the desired YouTube videos
import os, glob #Used for renaming and searching for files
import subprocess #Used for executing command line commands
import sys #Used for accessing command line arguements 
import shutil #Used for moving files between directories
from rich.console import Console #Used for customazation of the terminal

console = Console()

#Move the new mp3 file to the "Geomtry Dash" folder that contains all the related songs
def Move_to_gd(song_id, current_path, gd_song_path):
    os.chdir(current_path) #Change directory into the current_path
    if f"{song_id}.mp3" in glob.glob("*.mp3"): #Check if the song already exists in the current_path
        shutil.move(f"{song_id}.mp3", gd_song_path) #Will move it to gd_song_path

        #Print success message
        console.print(f"MOVED YOUR SONG TO {gd_song_path}, AS: {song_id}.mp3", style="bold green")
    else: #Will print an error message
        console.print(f"'{song_id}.mp3' WAS NOT FOUND IN THE CURRENT DIRECTORY: {current_path}", style="bold red")

    
#Renames the existing file at "gd_song_path"
def Rename_existing(song_id, gd_song_path):
    try:
        #Will rename the Newgrounds.com song so that it doesn't get lost
        os.rename(f"{gd_song_path}\\{song_id}.mp3", f"{gd_song_path}\\{song_id}-original.mp3")
        
        #Will print simple success message
        console.print(f"RENAMED THE ORIGINAL FILE AS: {song_id}-original.mp3", style="bold green")
    except FileExistsError:#Will print simple error message
        console.print(f"'{song_id}-original.mp3' ALREADY EXISTS IN: {gd_song_path}.", style="bold red")

def Replace(song_id, gd_song_path, current_path):
    os.chdir(gd_song_path) #Change directory into gd_song_path 

    #Wil check if file exists in in gd_song_path and act acordingly
    if f"{song_id}.mp3" in glob.glob("*.mp3"):
        Rename_existing(song_id, gd_song_path)
        
        Move_to_gd(song_id, current_path, gd_song_path)
    else:#Will just move it
        Move_to_gd(song_id, current_path, gd_song_path)

#Will identify and donwload the song:
def Download(url, current_path):
    video = pafy.new(url) #Search for the file

    #simple success message
    console.print(f"FOUND: {video.title}", style="bold green")

    audio = video.getbestaudio()#Get the best available audio
    os.chdir(current_path) #Change directory to current_path
    audio.download() #Download the audio

    return video

#Convert the song from webm to mp3 using ffmpeg
def Convert_to_mp3(video, song_id):
    # ffmpeg is a command line tool deticated to converting video and audio files

    # Will use the ffmpeg environment variable in order to convert the dowloaded audio from Download()
    # to an mp3 file that will be recognized by the game 
    subprocess.run(["ffmpeg", "-i", f"{video.title}.webm", f"{song_id}.mp3"], shell=True) #this code will execute the command

    #simple success message
    console.print(f"Converted {video.title}.webm to 'mp3'", style="bold green")


def main():

    #Variables:
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    current_path = os.getcwd()
    url = sys.argv[1] #Desired song
    song_id = sys.argv[2] #Provided song id

    video = Download(url, current_path)
    Convert_to_mp3(video, song_id)
    Replace(song_id, gd_song_path, current_path)

    os.remove(video.title + ".webm") #Will delete the initial audio file so that is doesn't take up space

if __name__ == '__main__':
    main()
