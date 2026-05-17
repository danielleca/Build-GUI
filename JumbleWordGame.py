import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = Tk()

words = {
    "plpea": "apple",
    "gnoma": "mango",
    "annaba": "banana",
    "hveeica": "achieve",
    "kaatko": "kolkata",
    "egvnine": "evening",
    "aestrv": "servant",
    "iceever": "receiver",
    "Lndono": "london",
    "rrreifa": "ferrari",
    "wllhoo": "hollow",
    "oohr": "horror",
    "rtemsa": "master",
    "nnrgimo": "morning",
    "Itbtoe": "bottle",
    "enp": "pen",
    "ourrte": "router",
    "ypco": "copy",
    "rraonw": "narrow",
    "wdie": "wide",
    "ievd": "dive",
    "elov": "love",
    "klboc": "block",
    "ightr": "right",
    "plmsie": "simple",
    "dea": "deaf",
    "gIneis": "single",
    "ghtkni": "knight",
    "opeh": "hope",
}

question_words = list(words.keys())

question = random.choice(question_words)

c = 0
d = 0
s = ""
l = Label(root)

def reset():
    global question
    question = random.choice(question_words)
    label.config(text = question)
    e1.delete()

def default():
    global question
    label.config(text = question)

def checkans():
    global question, c, d, s, l
    d = d + 1
    var = e1.get()
    var = var.lower()

    if var == words[question]:
        messagebox.showinfo("Congratulations","Its a correct answer!!"
        )
        c = c + 1
    
    else:
        messagebox.showerror("Sorry","Its not the correct answer")

    s = "Score: "+str(c) + "/"+ str(d)
    l.forget()
    l = Label(root, font=("Verdana", 20), text = s, bg="black", fg="white")
    l.pack(side=LEFT)
    reset()

root.geometry("500x500+500+150")
root.title("Jumpled Word Game")
root.configure(background="black")

Label(
    root,
    text = "JUMBLED WORD GAME",
    font = ("Verdana",28),
    bg="Black",fg="white"
).pack(pady=5)

label = Label(
    root,
    font = ("Verdana",22),
    bg="black",
    fg="white",
)
label.pack(pady=30,ipady=10,ipadx=10)
ans = StringVar()
e1=Entry(root, font = ("Verdana",20),textvariable=ans)
e1.pack(ipady =5,ipadx=5)

Button(
    root,
    text="Check",
    font=("Comic Sana ms",20),
    width =10,
    bg="#333945",
    fg="#45CE30",
    relief = GROOVE,
    command = checkans
).pack(pady=40)

Button(
    root,
    text="Reset",
    font=("Comic Sana ms",20),
    width =10,
    bg="#777E8B",
    fg="#E1DA00",
    relief = GROOVE,
    command = reset
).pack()

default()
root.mainloop()