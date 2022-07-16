import os, glob #Used for renaming and searching for files
import sys #Used for geting the comand line arguments
from rich.console import Console #Used for customiazation of the terminal
from rich.table import Table #Used for adding Tables

console = Console() #Better looking console

#Will print every mp3 file located inside gd_song_path
def print_all(gd_song_path, file_table):
    
    #Add the first column to the file_table that holds the index number of each file
    file_table.add_column("File Number", justify="center", style="cyan")
    #Add the second column to the file_table that holds the filename of each file
    file_table.add_column("File Name", justify="left", style="blue")

    os.chdir(gd_song_path) #Change directory into gd_song_path so that glob.glob() knows where to look at
    for index, file in enumerate(glob.glob("*.mp3")): #Will enumerate and get each mp3 file inside of gd_song_path
                        #Column:  1    |    2
        file_table.add_row(str(index + 1), file) #Will add a deticated row for each file

    console.print(file_table) #Print the file_table

#Will print every file that matches a given song_id
def print_file(gd_song_path, user_input, file_table):
    #Change directory into gd_song_path so that glob.glob() knows where to look at
    os.chdir(gd_song_path)

    temp = [] #Temporary list that will hold every mp3 file inside of gd_song_path
    for file in glob.glob("*.mp3"): #Loop through all of the files and filter mp3 files
        if user_input in file: #Check if the given user_input matches the filename 
            temp.append(file) #Will append the filename to temp

    if len(temp) != 0: #Check if there is at least one file that matches the user_input

        #Add the first column to the file_table that holds the index number of each file
        file_table.add_column("File Number", style="cyan", justify="center")
        #Add the second column to the file_table that holds the filename of each file
        file_table.add_column("File Name", justify="left", style="blue")

        #Simple succes message
        console.print(f"THE FOLLOWING FILES WERE FOUND IN {gd_song_path}: ", style="bold green", highlight=False)

        for index, file in enumerate(temp):
            #Add a row for every file in temp and populate it with the index and the filename
            file_table.add_row(str(index + 1), file)

        console.print(file_table)
    else: #Error message if no file matches user_input
        console.print(f"There is no '{user_input}' file in {gd_song_path}", style="bold red", highlight=False)


def main():
    #Path to folder that stores every song 
    gd_song_path = r"C:\Users\User\AppData\Local\GeometryDash"
    action = sys.argv[1] #Store the user's input

    file_table = Table(title=f"Files Matching '{action}'") #Create the Table

    #Will check the action veriable and act acordingly
    if action == "-a": #'-a' is a reserved command for executinng print_all()
        print_all(gd_song_path, file_table)
    else:
        print_file(gd_song_path, action, file_table)

if __name__ == '__main__':
    main()