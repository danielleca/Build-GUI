import tkinter
from tkinter import *
import random
from tkinter import messagebox

root=Tk()
riddles={}
file=open("Riddles.txt","r")

for line in file:
    line = line.strip()
    question, answer = line.split("|")
    riddles[question]=answer

file.close()

questions = list(riddles.keys())
question = random.choice(questions)
score = 0
total = 0
s = ""
l=Label(root)

def reset():
    global question
    question = random.choice(questions)
    riddle_label.config(text = question)
    e1.delete(0,END)

def default():
    global question
    riddle_label.config(text=question)

def checkans():
    global question,score,total,s,l
    total=total+1
    var=e1.get()
    var=var.lower()
    if var == riddles[question]:
        messagebox.showinfo("Correct", "You gave the correct answer!")
        score = score+1
    
    else:
        messagebox.showerror("Wrong", "Your answer is wrong!")

    s="Score: "+str(score)+"/"+str(total)
    l.forget()
    l=label(root, text=s,
            font=("Verdana",18),bg="black",fg="white")
    l.pack(side=LEFT)
    reset()

root.geometry("500x500+500+150")
root.title("Riddle Game")
root.config(background="black")

Label(
    root,
    text="RIDDLE QUIZ",
    font=("Verdana",28),
    bg="black",fg="white"
).pack(pady=10)

riddle_label=Label(
    root,
    font=("Verdana",18),
    bg="black",fg="white",
    wraplength=400
)
riddle_label.pack(pady=40,ipadx=10,ipady=10)

ans=StringVar()
e1=Entry(root, font=("Verdana",20),textvariable=ans)
e1.pack(ipady=5,ipadx=5)

Button(
    root,
    text="Submit Answer",
    font = ("Comic sans ms",18),
    width=15,
    bg="#333945",
    fg="#45CE30",
    relief=GROOVE,
    command=checkans
).pack(pady=40)

Button(
    root,
    text="Next Riddle",
    font = ("Comic sans ms",18),
    width=15,
    bg="#777E8B",
    fg="#E1DA00",
    relief=GROOVE,
    command=reset
).pack()

default()

root.mainloop()