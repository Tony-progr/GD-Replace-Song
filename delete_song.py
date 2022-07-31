import os
import sys
from rich.console import Console

console = Console() #Better looking console

def delete(gd_song_path, filenames):
    for filename in filenames:
        try: 
            os.remove(f"{gd_song_path}\\{filename}")
            console.print(f"Deleted '{filename}' successfuly", style="bold green", highlight=False) #Will print success message
        except FileNotFoundError: 
            console.print(f"'{filename}' does not exist!", style="bold red", highlight=False)    