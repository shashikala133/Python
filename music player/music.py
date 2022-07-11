import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("music player")
musicplayer.geometry('450x350')
directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer,font="cambria 14 bold",bg='cyan2',selectmode=tkr.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
pygame.init()
pygame.mixer.init()
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))  #setting song
    var.set(playlist.get(tkr.ACTIVE))                 #setting var to song
    pygame.mixer.music.play()                           #playing the particular track

def exitmusicplayer():      #exiting or stopping the music player
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

#creating buttons
Button_play=tkr.Button(musicplayer,height=3,width=5,text="play_music",font="cambria 14 bold",command=play,bg="limegreen",fg="black")
Button_stop=tkr.Button(musicplayer,height=3,width=5,text="stop_music",font="cambria 14 bold",command=exitmusicplayer,bg="red",fg="black")
Button_pause=tkr.Button(musicplayer,height=3,width=5,text="pause_music",font="cambria 14 bold",command=pause,bg="yellow",fg="black")
Button_resume=tkr.Button(musicplayer,height=3,width=5,text="resume_music",font="cambria 14 bold",command=resume,bg="pink",fg="black")
Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both",expand="yes")

var=tkr.StringVar()
songtitle=tkr.Label(musicplayer,font="cambria 12 bold",textvariable="var")
songtitle.pack()
musicplayer.mainloop()
