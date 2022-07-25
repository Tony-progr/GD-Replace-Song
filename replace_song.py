import pafy #Used for finging and dowloading the desired YouTube videos
import os, glob #Used for renaming and searching for files
import subprocess #Used for executing command line commands
import sys #Used for accessing command line arguements 
import shutil #Used for moving files
from rich.console import Console #Used for customazation of the terminal

console = Console()

#Move the new mp3 file to the "Geomtry Dash" folder that contains all the related songs
def Move_to_gd(song_id, current_path, gd_song_path):
    os.chdir(current_path) #Change directory into the current_path
    if f"{song_id}.mp3" in glob.glob("*.mp3"): #Check if the song already exists in the current_path
        try:
            shutil.move(f"{song_id}.mp3", gd_song_path) #Will move it to gd_song_path

            #Print success message
            console.print(f"Moved your song to: {gd_song_path}", style="bright_black", highlight=False)
        except shutil.Error as e: #Handle latter
            print(e)

def overwrite_existing(song_id, gd_song_path):
    console.print(f"Overwriting...", style="yellow")
    
    #Remove existing song_id.mp3 file
    os.remove(f"{gd_song_path}\\{song_id}.mp3")
    console.print(f"Removed '{song_id}.mp3' from: {gd_song_path}", style="bright_black", highlight=False)

def dont_overwrite(song_id, current_path):
    console.print(f"Not overwriting...", style="yellow")

    os.remove(f"{current_path}/{song_id}.mp3")
    console.print(f"Removed {song_id}.mp3 from {current_path}.", style="bright_black", highlight=False)



#Renames the existing file at "gd_song_path"
def Rename_existing(song_id, current_path ,gd_song_path):
    try:
        #Will rename the Newgrounds.com song so that it doesn't get lost
        os.rename(f"{gd_song_path}\\{song_id}.mp3", f"{gd_song_path}\\{song_id}-original.mp3")
        
        #Will print simple success message
        console.print(f"Renamed the original file to: {song_id}-original.mp3", style="bright_black", highlight=False)
    except FileExistsError:#Will print simple error message
        console.print(f"The id: {song_id}, has alrady been replaced before.", style="bold red", highlight=False)
        console.print(f"Do you want to override the previous replacement? (y/n)", style="bright_black")
        user_answer = input("")
        print("\n")

        if user_answer in "yes" or user_answer in "YES":
            overwrite_existing(song_id, gd_song_path)
        elif user_answer in "no" or user_answer in "NO":
            dont_overwrite(song_id, current_path)
        else:
            console.print(f"Invalid Input! Enter: y (yes) or n (no).", style="bold red")


def Replace(song_id, gd_song_path, current_path):
    os.chdir(gd_song_path) #Change directory into gd_song_path 

    #Wil check if file exists in in gd_song_path and act acordingly
    if f"{song_id}.mp3" in glob.glob("*.mp3"):
        Rename_existing(song_id, current_path, gd_song_path)
        
        Move_to_gd(song_id, current_path, gd_song_path)
    else:#Will just move it
        Move_to_gd(song_id, current_path, gd_song_path)

#Will identify and donwload the song:
def Download(url, current_path):
    video = pafy.new(url, callback=None) #Search for the file

    #simple success message
    console.print(f"Found: {video.title}", style="bold green")

    audio = video.getbestaudio()#Get the best available audio
    os.chdir(current_path) #Change directory to current_path
    audio.download() #Download the audio
    print("\n")

    return video

#Convert the song from webm to mp3 using ffmpeg
def Convert_to_mp3(video, song_id):
    # ffmpeg is a command line tool deticated to converting video and audio files

    # Will use the ffmpeg environment variable in order to convert the dowloaded audio from Download()
    # to an mp3 file that will be recognized by the game 
    subprocess.run(["ffmpeg", "-i", f"{video.title}.webm", f"{song_id}.mp3", "-hide_banner", "-loglevel", "error"], shell=True) #this code will execute the command

    #simple success message
    console.print(f"Converted: {video.title}.webm to 'mp3'", style="bright_black", highlight=False)


def main():
    #Variables:
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    current_path = os.getcwd()
    url = sys.argv[1] #Desired song
    song_id = sys.argv[2] #Provided song id
    try:
        video = Download(url, current_path)
        Convert_to_mp3(video, song_id)
        Replace(song_id, gd_song_path, current_path)

        print("\n")
        console.print(f"The operation was successful!", style="bold green")
    except Exception as e:
        print(e)
    finally:
        try:
            #Will delete the initial audio file so that is doesn't take up space
            os.remove(video.title + ".webm") 
        except UnboundLocalError:
            pass
        
if __name__ == '__main__':
    main()
