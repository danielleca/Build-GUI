from tkinter import *

root = Tk()
root.title("Theme Changer")
root.geometry("400x300")

color_var = StringVar(value= "red")

def change_color():
    root.config(bg= color_var.get())

label = Label(root,text = "Change Background Color:", font=("Arial",12))
label.pack(pady = 20)

frame = Frame(root)
frame.pack()

r1 = Radiobutton(frame, text = "Red", variable= color_var, value= "red", command=change_color)
r1.pack(anch = "w")
r2 = Radiobutton(frame, text = "Green", variable= color_var, value= "green", command=change_color)
r2.pack(anch = "w")
r3 = Radiobutton(frame, text = "Blue", variable= color_var, value= "blue", command=change_color)
r3.pack(anch = "w")

root.config(bg="red")
root.mainloop()