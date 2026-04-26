from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

window = Tk()
window.title("speech to text")
window.geometry("100x400")

heading1 = Label(window, text = "Voice Notepad", font = ("Arial", 30, "bold"))
heading1.grid(row=0,column=1,padx=20,pady=20)

Output_text = Text(window, height=6,width=40,font=("Arial",12))
Output_text.grid(row=1,column=1,pady=20,padx=20)

def Translate():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except:
            text = "Sorry could not recognize your voice"
    
    Output_text.delete(1.0, END)
    Output_text.insert(END, text)

def save():
    fout = asksaveasfile(defaultextension=".txt")
    if fout:
        fout.write(Output_text.get(1.0, END))
        fout.close()
        messagebox.showinfo("Saved", "File saved successfully.")

    else:
        messagebox.showinfo("Warning", "Text not saved.")

trans_btn = Button(
    window,
    text="Click Me!\nStart Recording",
    command = Translate,
    font = ("Arial", 15, "bold"),
    width =20,
    bg= "#4CAF50",
    fg="white" 
)

trans_btn.grid(row=1,column=0,pady=20,padx=20)

save_button = Button(
    window,
    text= "Save the text",
    font = ("Arial",12,"bold"),
    command=save,
    width=20,
    height=4,
    bg = "#2196F3",
    fg ="white"
)
save_button.grid(row=1,column=2,pady=10)
window.mainloop()