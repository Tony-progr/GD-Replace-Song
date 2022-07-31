import os, glob #Used for renaming and searching for files
import sys #Used for geting the comand line arguments
from rich.console import Console #Used for customiazation of the terminal
from rich.table import Table #Used for adding Tables

console = Console() #Better looking console

#Will print every mp3 file located inside gd_song_path
def print_all(gd_song_path, file_table):
    
    file_table.add_column("File Number", justify="center", style="cyan")
    file_table.add_column("File Name", justify="left", style="blue")

    os.chdir(gd_song_path)
    for index, file in enumerate(glob.glob("*.mp3")):
        file_table.add_row(str(index + 1), file)

    console.print(file_table)

#Will print every file that matches a given song_id
def print_file(gd_song_path, user_input, file_table):
    os.chdir(gd_song_path)

    temporary = []
    for file in glob.glob("*.mp3"):
        if user_input in file: 
            temporary.append(file)

    #Check if there exists at least one file
    if len(temporary) != 0: 

        file_table.add_column("File Number", style="cyan", justify="center")
        file_table.add_column("File Name", justify="left", style="blue")

        console.print(f"The following files were found:", style="bold green")

        for index, file in enumerate(temporary):
            file_table.add_row(str(index + 1), file)

        console.print(file_table)
    else:
        console.print(f"There is no '{user_input}' file in {gd_song_path}", style="bold red")