'''
School Project by Animesh Bhatt 
Class - 11th A
Roll no. - 1
Date - 19th Feb 2021
Program - Interactive text file reader & save as MP3
'''
import pyttsx3 as tts
import tkinter
from tkinter import filedialog
from tkinter import *


# setting properties of the tkinter GUI
root = Tk()
root.title("Interactive text file reader & save as MP3")
root.resizable(0, 0)


# setting properties of the pyttsx3
talk = tts.init()
rate = talk.getProperty('rate')
talk.setProperty('rate',190)
volume = talk.getProperty('volume')
talk.setProperty('volume',1.0)

file_text = "" #empty string

def male():
    voices = talk.getProperty('voices')  # getting details of current voice
    talk.setProperty('voice', voices[0].id) #male voice
    talk.say("Male voice Selected")
    talk.runAndWait()

def female():
    voices = talk.getProperty('voices')  # getting details of current voice
    talk.setProperty('voice', voices[1].id) #female voice
    talk.say("Female voice Selected")
    talk.runAndWait()

def default():
    voices = talk.getProperty('voices')  # getting details of current voice
    talk.setProperty('voice', voices[0].id) #male voice
    talk.say("Male voice selected by default")
    talk.runAndWait()

def filechooser():
    global filename #making the variable global
    root.filename = filedialog.askopenfilename(initialdir="C:", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    filename = root.filename #get filename
    print(filename)
    with open(root.filename, "r") as f:
        global file_text
        file_text = f.read()
        Label(root, text=file_text, borderwidth=2, relief="groove",font=("Veranda", 12))\
            .grid(row=6,column=5,pady=10,padx=10)
        def filespeak():
            talk.say(file_text)
            talk.runAndWait()

        def save_audio():
            talk.save_to_file(file_text,filename+".mp3")
            talk.runAndWait()

        Button(root,text="Read text", command= filespeak).grid(row=7,column=5,pady=5,padx=20)
        Button(root, text="Save audio", command=save_audio).grid(row=8,column=5,pady=5,padx=20)


# Main code; it executes and works according to the button pressed
Label(root,text="Interactive text file reader",font=("Times", 20)).grid(row=0,column=5,ipadx=10)
Label(root,text="*(optional) Choose a speaker: ").grid(row=1,column=5,pady=15)
Button(root, text ="Male", command = male).grid(row=2,column=5,pady=5)
Button(root, text ="Female", command = female).grid(row=3,column=5,pady=5)
Button(root, text ="Reset to Default", command = default).grid(row=4,column=5,pady=5)
Button(root,text="Choose a text file", command = filechooser,font=("Trajan", 11))\
    .grid(row=5,column=5,pady=10,padx=50)



mainloop()  #starts the tkinter GUI
