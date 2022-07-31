from rich.console import Console
from rich.table import Table
import sys

console = Console()

def check_for_song(gd_song_path, action):
    from check_song import print_all, print_file

    file_table = Table(title=f"Files Matching '{action}'")

    if action == "-a":
        print_all(gd_song_path, file_table)
    else:
        print_file(gd_song_path, action, file_table)

def delete_the_song(gd_song_path, action):
    from delete_song import delete

    delete(gd_song_path, action)

def open_the_song_directory(gd_song_path):
    from directory_song import open_directory

    open_directory(gd_song_path)

def revert_to_original(gd_song_path, action):
    from revert_song import revert_to

    revert_to(gd_song_path, action)

def replace_original_song(gd_song_path, song_url, original_song_id):
   from replace_song import new_replacement

   new_replacement(gd_song_path, song_url, original_song_id)

def main():
    try:
        action = sys.argv[1:]
        gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"

        if action[0] == "-r":
            try:
                song_url = action[1]
                original_song_id = action[2]
            except IndexError:
                console.print("You need to provide both a vaild ULR and song_id!", 
                                style="bold red")

            replace_original_song(gd_song_path, song_url, original_song_id)
        elif action[0] == "-d":
            try:
                filename = action[1:]
            except IndexError:
                console.print("You need to provide a vaild filename(s)!",
                                style="bold red")

            delete_the_song(gd_song_path, filename)
        elif action[0] == "-rv":
            try:
                filename = action[1]
            except IndexError:
                console.print("You need to provide a vaild filename",
                                style="bold red")

            revert_to_original(gd_song_path, filename)
        elif action[0] == "-o":

            open_the_song_directory(gd_song_path)
        elif action[0] == "-c":
            try:
                parameter = action[1]
            except IndexError:
                console.print("Please input a valid search parameter!",
                                style="bold red")

            check_for_song(gd_song_path, parameter)
        else:
            console.print(f"Invalid flag: '{action[0]}'", style="red bold")
    except IndexError:
        console.print("Not enough arguments provided!", style="bold red")
 
if __name__ == '__main__':
    main()




    
