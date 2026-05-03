import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

def listen_password():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...",fg="blue")
            root.update()

            audio=recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            print("You said...",text)
            check_password(text)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio")
        status_label.config(text="status: LOCKED", fg= "red")
    except sr.RequestError:
        messagebox.showerrpr("Error","Speech service error")

def check_password(text):
    if text.lower() == "open":
        status_label.config(text="Status: UNLOCKED", fg="green")
        messagebox.showinfo("Access","Access Granted")
    else:
        status_label.config(text="Status: LOCKED", fg = "red")
        messagebox.showwarning("Access","Access Denied")

root =tk.Tk()
root.title("Voice Vault")
root.geometry("400x250")
root.configure(bg="black")

status_label=tk.Label(
    root, text = "Status: LOCKED", fg = "red",bg="black", font=("Arial", 16, "bold")

)
status_label.pack(pady=40)

speak_btn = tk.Button(
    root,
    text = "Speak Password",
    command = listen_password,
    font=("Arial",12),
    bg="blue",
    fg="white",
    padx=10,
    pady=5
)
speak_btn.pack()
root.mainloop()