from tkinter import *
from gtts import gTTS
import os

window = Tk()
frame1 = Frame(window, bg = "lightpink", height = 150)
frame1.pack(fill = X)

frame2 = Frame(window, bg = "lightgreen", height = 750)
frame2.pack(fill = X)

label = Label(frame1, text = "Text to Speech", font = "bold, 30", bg = "lightpink")
label.place(x = 180, y= 70)

entry = Entry(frame2, width = 45, bd = 4, font = 14)
entry.place(x = 50, y=52)
entry.insert(0, "")

def play():
    language = "es"
    myObj = gTTS(text = entry.get(), lang = language, slow = False, tld = "co.za")
    myObj.save("convert.wav")
    os.system("convert.wav")

btn = Button(frame2, text = "SUBMIT", width = 15, pady = 10, font = "bold, 15", 
             command = play, bg = "yellow")
btn.place(x = 250, y = 130)
window.title("Text to speech")
window.geometry("650x550+350+200")
window.mainloop()