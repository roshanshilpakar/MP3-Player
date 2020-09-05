from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")


#function to add one song
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose a song" , filetypes=(("mp3 Files" , "*.mp3"), ("m4a Files", "*.m4a")))
	#my_label.config(text=song)

	#strip out directory and .extensions from the song title
	song = song.replace("G:/mp3/audio/" , "")
	song = song.replace(".mp3" , "")

	song = song.replace("G:/m4a/audio/" , "")
	song = song.replace(".m4a" , "")

	playlist_box.insert(END , song)

#function to add many songs
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose a song" , filetypes=(("mp3 Files" , "*.mp3"), ("m4a Files", "*.m4a")))
	#my_label.config(text=song)

	# loop through the song list and rep;ace  directort structure
	for song in songs:
		#strip out directory and .extensions from the song title
		song = song.replace("G:/mp3/audio/" , "")
		song = song.replace(".mp3" , "")

		song = song.replace("G:/m4a/audio/" , "")
		song = song.replace(".m4a" , "")
        # add to end playlist
		playlist_box.insert(END , song)

#function to delete one song
def delete_song():
	#delete highlighted song form the playlist
	playlist_box.delete(ANCHOR)

#function to delete one song
def delete_all_songs():
	playlist_box.delete(0 , END)


# create Playlist Box
playlist_box = Listbox(root, bg="black", fg="green", width=60 , selectbackground= "white" , selectforeground = "black" )
playlist_box.pack(pady=20)

# Define Button Images For Controls
backward_button_img = PhotoImage(file='images/backward.png')
forward_button_img = PhotoImage(file='images/forward.png')
play_button_img = PhotoImage(file='images/play.png')
pause_button_img = PhotoImage(file='images/pause.png')
stop_button_img = PhotoImage(file='images/stop.png')

# Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20)


# Create Play/Pause and otherButtons
backward_button = Button(control_frame, image = backward_button_img, borderwidth = 0)
forward_button = Button(control_frame, image = forward_button_img, borderwidth = 0)
play_button = Button(control_frame, image = play_button_img, borderwidth = 0)
pause_button = Button(control_frame, image = pause_button_img, borderwidth = 0)
stop_button = Button(control_frame, image = stop_button_img, borderwidth = 0)


backward_button.grid(row=0, column = 0 , padx = 10)
forward_button.grid(row=0, column = 1, padx = 10)
pause_button.grid(row=0, column = 3, padx = 10)
play_button.grid(row=0, column = 2, padx = 10)
stop_button.grid(row=0, column = 4, padx = 10)


# Create  main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdowns
add_song_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label=" Add Songs", menu= add_song_menu)
# add one song in the playlist
add_song_menu.add_command(label="Add one song to the playlist", command = add_song)
# add more songs in the playlist
add_song_menu.add_command(label="Add many songs to the playlist", command = add_many_songs)

 # Delete songs menu
remove_song_menu = Menu(my_menu , tearoff =0)
my_menu.add_cascade(label="Remove songs", menu = remove_song_menu)
remove_song_menu.add_command(label="Delete a song from playlist" , command = delete_song)
remove_song_menu.add_command(label="Delete all songs from playlist" , command = delete_all_songs)

# temporary label 
my_label = Label(root , text = '')
my_label.pack(pady=20)






root.mainloop()