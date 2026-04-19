from tkinter import *
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

root = Tk()
entry = Entry(root, width = 40, font = 14)
entry.pack(pady = 20)

def speak():
    text = entry.get()
    latvian_text = GoogleTranslator(source = "en", target = "es").translate(text)
    speech = gTTS(text = latvian_text, lang = "es")
    speech.save("latvian.mp3")
    os.system("latvian.mp3")

btn = Button(root, text = "speak in Latvian", command = speak)
btn.pack(pady = 20)
root.mainloop()