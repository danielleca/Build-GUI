from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Student Registration")
window.geometry("400x300")
window.configure(bg = "lightblue")

heading = Label(
    window,
    text = "Coding Class Registration",
    font = ("Arial", 16, "bold"),
    bg = "lightblue"
)

heading.grid(row = 0, column = 0, columnspan = 2, pady = 15)

courseLabel = Label(
    window,
    text= "Select your Course: ",
    bg="lightblue"
)

courseLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = E)

courseVar = StringVar()

courseCombo = Combobox(
    window,
    textvariable=courseVar,
    state = "readonly"
)

courseCombo["values"] = ("Python", "Game Development", "Web development", "Ai")
courseCombo.grid(row = 1, column =1, pady = 10)

batchLabel = Label(
    window,
    text= "Select Batch Timing: ",
    bg = "lightblue"
)
batchLabel.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = E)
batchVar = StringVar()

morningRB = Radiobutton(
    window,
    text = "Morning Batch",
    variable = batchVar,
    value = "Morning Batch",
    bg = "lightblue"
)

eveningRB = Radiobutton(
    window,
    text = "Evening Batch",
    variable = batchVar,
    value = "Evening Batch",
    bg = "lightblue"
)

morningRB.grid(row = 2, column = 1, sticky = W)
eveningRB.grid(row = 3, column = 1, sticky = W)

batchVar.set("Morning Batch")

def enroll():
    course = courseVar.get()
    batch = batchVar.get()

    resultLabel.config(
        text = f"Registered for {course} in the {batch}"
    )

enrollBtn = Button(
    window,
    text = "Enroll Now",
    command = enroll,
    bg = "dark blue",
    fg = "white",
    padx = 10,
    pady = 5
)

enrollBtn.grid(row = 4, column = 0, columnspan = 2, pady = 15)

resultLabel = Label(
    window,
    text = "",
    bg = "lightblue",
    font = ("Arial", 10, "bold"),
    fg = "green"
)

resultLabel.grid(row = 5, column = 0, columnspan=2)

window.mainloop()