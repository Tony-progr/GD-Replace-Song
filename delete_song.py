import os
import sys
from rich.console import Console

console = Console() #Better looking console

def main():
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash" #Path to the folder that stores the songs for the game
    filenames = sys.argv[1:] #Create a list with every filename

    for filename in filenames: #Loops through the filenemes list
        try: 
            os.remove(f"{gd_song_path}\\{filename}") #Will remove the file
            console.print(f"Deleted '{filename}' successfuly", style="bold green", highlight=False) #Will print success message
        except FileNotFoundError: 
            #Will print an error message for every file that doesn't exist in gd_song_path
            console.print(f"'{filename}' does not exist!", style="bold red", highlight=False)    

if __name__ == '__main__':
    main()