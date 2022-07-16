import os
import sys
from rich.console import Console

console = Console()

def main():
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    filenames = sys.argv[1:]

    for filename in filenames:
        try:
            os.remove(f"{gd_song_path}\\{filename}")
            console.print(f"Deleted '{filename}' successfuly", style="bold green", highlight=False)
        except FileNotFoundError:
            console.print(f"'{filename}' does not exist!", style="bold red", highlight=False)    

if __name__ == '__main__':
    main()