from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()

root.title("MP3 Player")
root.geometry("500x500")

#initilize pygame 
pygame.mixer.init()

# cerate function to deal with time
def play_time():
	# check to see if song is stopped
	if stopped:
		return


	#grab current song time
	current_time = pygame.mixer.music.get_pos() / 1000
	#time format
	converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))

	song = playlist_box.get(ACTIVE)
	song = f'G:/mp3/audio/{song}.mp3'

	#find the current song length
	song_mut = MP3(song)
	global song_length
	song_length = song_mut.info.length
	#convert to time format
	converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))
	#my_label.config(text=converted_song_length)

	#check if the song is over
	if int(song_slider.get()) == int(song_length):
		next_song()

	elif paused:
		pass
	else:
		#move slider along 1 second at a time
		next_time = int(song_slider.get()) + 1
		#output new time value to slider and to length
		song_slider.config(to=song_length,value=next_time)
		#COnvert slider position to time format
		converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(song_slider.get())))

		#output slider
		status_bar.config(text=f'Time Elapsed : {converted_current_time} Of {converted_song_length} ')



	if current_time > 0:
	#current time to status bar
		status_bar.config(text=f'Time Elapsed : {converted_current_time} Of {converted_song_length} ')
	#check loop every second
	status_bar.after(1000,play_time)





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

# create play funtion
def play():
	#set stop to false since a song is now playing
	global stopped
	stopped = False

	#reconstruct song eith directory steuture
	song = playlist_box.get(ACTIVE)
	song = f'G:/mp3/audio/{song}.mp3'

	#my_label.config(text=song)

	#load song with pygame mixer
	pygame.mixer.music.load(song)

	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	#get song time
	play_time()


#create stopped varibale
global stopped
stopped = False

#create stop function
def stop():
	#stop the song
 	pygame.mixer.music.stop()
 	#clear playlist bar
 	playlist_box.selection_clear(ACTIVE)

 	status_bar.config(text='')

 	#set stop varibale to True
 	global stopped
 	stopped = True

# create oaused variable
global paused
paused = False

 # create pause function
def pause(is_paused):
	global paused 
	paused = is_paused

	if paused:
		#unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		#pause
		pygame.mixer.music.pause()
		paused = True


#create next song function
def next_song():
	# reset slider position and status bar
	status_bar.config(text='')
	song_slider.config(value=0)
	#get current song number
	next_one = playlist_box.curselection()
	#add 1 to the current song
	next_one = next_one[0] + 1

	#grab song title from the playlist
	song = playlist_box.get(next_one)
	# add directory structure stuff to the song
	song = f'G:/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)

	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	#clear active bar in playlist
	playlist_box.selection_clear(0, END)

	#move active bar to next song
	playlist_box.activate(next_one)

	#set the active bar to the next song
	playlist_box.selection_set(next_one , last=None)


#create previous song function
def previous_song():
	# reset slider position and status bar
	status_bar.config(text='')
	song_slider.config(value=0)
	#get current song number
	next_one = playlist_box.curselection()
	#add 1 to the current song
	next_one = next_one[0] - 1

	#grab song title from the playlist
	song = playlist_box.get(next_one)
	# add directory structure stuff to the song
	song = f'G:/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)

	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	#clear active bar in playlist
	playlist_box.selection_clear(0, END)

	#move active bar to next song
	playlist_box.activate(next_one)

	#set the active bar to the next song
	playlist_box.selection_set(next_one , last=None)


#create volume function
def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())
#create main frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# create slide function
def slide(x):
	song = playlist_box.get(ACTIVE)
	song = f'G:/mp3/audio/{song}.mp3'

	#my_label.config(text=song)

	#load song with pygame mixer
	pygame.mixer.music.load(song)

	#play song with pygame mixer
	pygame.mixer.music.play(loops=0, start=song_slider.get())


# create Playlist Box
playlist_box = Listbox(main_frame, bg="black", fg="green", width=60 , selectbackground= "white" , selectforeground = "black" )
playlist_box.grid(row=0,column=0)

#create volume slider frame
volume_frame = LabelFrame(main_frame,text="Volume ")
volume_frame.grid(row=0, column=1)

# create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL , length=125, command=volume, value=1)
volume_slider.pack(pady=10)


#create song slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL , length=360, command=slide, value=0)
song_slider.grid(row=2,column=0, pady=20)


# Define Button Images For Controls
backward_button_img = PhotoImage(file='images/backward.png')
forward_button_img = PhotoImage(file='images/forward.png')
play_button_img = PhotoImage(file='images/play.png')
pause_button_img = PhotoImage(file='images/pause.png')
stop_button_img = PhotoImage(file='images/stop.png')

# Create Button Frame
control_frame = Frame(main_frame)
control_frame.grid(row=1,column=0,pady=20, padx=20)


# Create Play/Pause and otherButtons
backward_button = Button(control_frame, image = backward_button_img, borderwidth = 0 , command = previous_song)
forward_button = Button(control_frame, image = forward_button_img, borderwidth = 0 , command = next_song)
play_button = Button(control_frame, image = play_button_img, borderwidth = 0,command=play)
pause_button = Button(control_frame, image = pause_button_img, borderwidth = 0, command = lambda: pause(paused))
stop_button = Button(control_frame, image = stop_button_img, borderwidth = 0, command=stop)


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


# create status bar
status_bar = Label(root , text = '' , bd= 1 , relief = GROOVE , anchor = E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)






root.mainloop()