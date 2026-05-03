from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

w = Tk()
w.title("Voice Colors")
w.geometry("500x200")

lbl = Label(w,text="Say a color name: ")
lbl.pack()

colors = {
    "red":"red",
    "read" : "red",
    "blue":"blue",
    "blew":"blue",
    "green":"green",
    "black":"black",
    "yellow":"yellow"

}

def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print("You said: ", text)
            if text in colors:
                w.config(bg=colors[text])
            else:
                messagebox.showinfo("Error", "Color not recognized")
        except:
            messagebox.showinfo("Voice not recognized", "Please try again")

btn = Button(
    w, text = "Listen", width=15,bg="#475C95",
    fg="white",command=Listen,
)
btn.pack()
w.mainloop()