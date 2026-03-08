from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Multiplication Table Generator")
title = Label(window, text = "Multiplication Table")
caption = Label(window, text = "Number and Range: ")
title.grid(row = 0, column = 0, columnspan = 3, pdy = 25)
caption.grid(column = 0, row = 1, padx = 10)
theNum = IntVar() #Combobox
numbers = Combobox(window, textvariable=theNum, width = 5)
numbers["Values"] = tuple(range(101))
endVal = IntVar() #RadioButton
r10 = Radiobutton(window, text = "10", variable=endVal, value = 10)
r20 = Radiobutton(window, text = "10", variable=endVal, value = 20)
r30 = Radiobutton(window, text = "10", variable=endVal, value = 30)