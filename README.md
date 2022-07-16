# GD-Replace-Song
This is a CLI tool writen in python that manipulates the game files of Geometry Dash in order to provide a simpler way of using custom songs within the game. This saves
the players a lot of time and prevents them from doing simple but boring and tedious tasks. Keep reading in order to understand how is this useful.

# Why is it useful?
Geometry dash is a music-based platformer game, wich means that music plays a huge role in the experience of the player. The game (apart from the 21 "main songs" that
are installed along with the game) uses Newgrounds.com as the main source of music for players to use in-game. However, Newgrounds.com doesn't have a big enough music
selection to satisfy the comunity, so palyers download songs from YouTube.com and then "import" them into the game by manipulating the game files. This process is done
manually and is rahter tedious. This tool aims towards automating this process and leting the players enjoy the game.

# How does it work?
Firstly let's take a look on how the players manipulate the game files:
Every song on Newgrounds.com has a unique ID which can be found at the end of the song's URL. After dowloading the song (using a feature within the game) it will be saved
as '{song_id}.mp3' inside a 'Geometry Dash' folder located deep into the hiden 'AppData' directory. (*Windows 10/11). (example: if the song's ID was 1000 it would be 
saved as '1000.mp3'). After navigating to that 'buried' folder players would have to replace '{song_id}.mp3' with their desired song and save it under the same exact name.
This way the player would be able to use their favourite songs inside the game despite them not being avalable on Newgournds.com.

Now let's see what these python scripts do:
1. replace_song.py: Given a YouTube link and a song ID. Will download the YouTube video as a "webm" file (using the pafy pip module) and will then convert it into an "mp3" 
file (using ffmpeg) since that is the only format the the game is able to read. Then it will rename the '{song_id}.mp3' file (*original song) into '{song_id}-original.mp3'
(this is for safe-keeping incase the original is needed) and move the user's desired YouTube song into the 'Geometry Dash' folder and name it '{song_id}.mp3' so the game 
recognizes it as the original.
2. check_song.py: Given a song ID or a spesific arguement. Will print every file inside the 'Geometry Dash' folder that matches the ID/arguemnet.
3. delete_song.py: Given a filename (example: '190874.mp3'). Will delete the spesified file if it exists.

# How to use:
1. (required) You will have to dowload ffmpeg and then add it to 'PATH'.
2. (optional) You can add these scripts to 'PATH' so that you can run them from anywhere in your system.

After dowloading the scripts, this is how you use each script. (inside your terminal):
1. replace_song.py: C:\Users\User>replace_song.py <YoutTube link> <Newgounds song id>
2. check_song.py: C:\Users\User>check_song.py <ID or arguement> 
(a valid arguement is -a which prints every mp3 file)\
3. delete_song.py: C:\Users\User>delete_song.py <filename>
(use check_song.py to see all files)
