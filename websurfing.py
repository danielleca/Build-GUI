import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import webbrowser
def voice_search():
    recognizer = sr. Recognizer()
    try:
        with sr.Microphone() as source:
            status_label.config(text="listening...",fg="pink")
            root.update()
            audio=recognizer.listen(source)
            text=recognizer.recognize_google(audio)
            print("You said: ",text)
            open_google(text)
    except sr.UnknownValueError:
        messagebox.showerror("Error","Could not understand audio")
        status_label.config(text="Try again",fg="red")
    except sr.RequestError:
        messagebox.showerror("Error","Speech service unavailable")

def open_google(query):
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    status_label.config(text=f"Searching: {query}", fg="green")

root=tk.Tk()
root.title("Voice Search")
root.geometry("450x250")
root.configure(bg="black")

title_label=tk.Label(
    root,
    text="What do you want to search? ",
    fg = "white",
    bg = "black",
    font=("Arial",14,"bold")
)
title_label.pack(pady=20)

status_label=tk.Label(
    root,
    text="click the button and speak",
    fg="grey",
    bg="black",
    font=("Arial",12,"bold"),
)
status_label.pack(pady=10)
search_btn=tk.Button(
    root,
    text="Search Google",
    command=voice_search,
    font=("arial",12,"bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5
)
search_btn.pack(pady=20)
root.mainloop()