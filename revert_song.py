#Will revert from a custom song back to the original 
#(Will rename {song_id}-original.mp3 to {song_id}.mp3)

import sys
import os
from rich.console import Console
from glob import glob

console = Console()


def revert(filename, gd_song_path):
    raw_filename = filename.split(".")
    os.chdir(gd_song_path)
    file_list = glob("*.mp3")
    
    if filename in file_list: 
        if f"{raw_filename[0]}-original.mp3" in file_list:
            console.print("Working on it...", style="yellow")

            os.remove(f"{gd_song_path}\{filename}") #Removes {song_id}.mp3
            console.print(f"Removed '{filename}' from {gd_song_path}.", style="bright_black")

            raw_filename = filename.split(".")
            #Rename {song_id}-original.mp3 to {song_id}.mp3
            os.rename(f"{gd_song_path}\{raw_filename[0]}-original.mp3", f"{gd_song_path}\{filename}")
            console.print(f"Renamed '{raw_filename[0]}-original.mp3' to '{filename}'", style="bright_black")
            
            console.print("The opperation was successful!", style="bold green")
        else:
            console.print(f"Can't revert back to '{filename}' since it has not been replaced before.", style="bold red")
    else:
        console.print(f"There is no '{filename}' in {gd_song_path}", style="bold red")

def main():
    try:
        gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
        filename = sys.argv[1] 

        revert(filename, gd_song_path)
    except IndexError:
        console.print("Error! You need to input a valid filename as an argument!", style="bold red")

if __name__ == '__main__':
    main()