import os, glob
import sys
from colorama import Fore
import fnmatch
from rich.console import Console
from rich.table import Table

console = Console()

def print_all(gd_song_path, file_table):
    os.chdir(gd_song_path)

    file_table.add_column("File Number", justify="center", style="cyan")
    file_table.add_column("File Name", justify="left", style="blue")

    for index, file in enumerate(glob.glob("*.mp3")):
        file_table.add_row(str(index + 1), file)

    console.print(file_table)

def print_file(gd_song_path, input_, file_table):
    os.chdir(gd_song_path)

    temp = []
    for file in glob.glob("*.mp3"):
        if input_ in file:
            temp.append(file)

    if len(temp) != 0:
        file_table.add_column("File Number", style="cyan", justify="center")
        file_table.add_column("File Name", style="blue")

        console.print(f"THE FOLLOWING FILES WERE FOUND IN {gd_song_path}: ", style="bold green", highlight=False)

        for index, file in enumerate(temp):
            file_table.add_row(str(index + 1), file)

        console.print(file_table)
    else:
        console.print(f"The is no '{input_}' file in {gd_song_path}", style="bold red", highlight=False)


def main():

    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    action = sys.argv[1]

    file_table = Table(title=f"Files Matching '{action}'")

    if action == "-a":
        print_all(gd_song_path, file_table)
    else:
        print_file(gd_song_path, action, file_table)

if __name__ == '__main__':
    main()