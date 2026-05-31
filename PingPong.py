from tkinter import *
import random
from tkinter import messagebox

win = Tk()
win.title("Ping Pong Game")
win.resizable(0,0)
canvas_width = 600
canvas_height = 500
canvas = Canvas(win, width=canvas_width,height=canvas_height,
                 bg="black")
canvas.pack()
canvas.focus_set()
score_font=("Arial",20,"bold")
scoring_text=canvas.create_text(
    300, 20, font=score_font,
    text="0 : 0",fill="blue"
)
canvas.create_line(canvas_width/2,0,canvas_width/2,canvas_height,
                   fill="white")
x=canvas_width/2
y=canvas_height/2
r=50
canvas.create_oval(x - r, y - r, x+r, y+r,outline="white")
paddle_width=20
paddle_height=80
class Paddle:
    def __init__(self,canvas,color,x,y):
        self.canvas=canvas
        self.paddle=canvas.create_rectangle(
            x, y, x+paddle_width, y+paddle_height, fill=color
        )
        self.delta=0

    def moveUpDownUsing(self, up_key, down_key):
        self.canvas.bind_all(up_key, self.moveUp)
        self.canvas.bind_all(down_key, self.moveDown)

    def draw(self):
        self.canvas.move(self.paddle, 0, self.delta)
        pos = self.canvas.coords(self.paddle)
        if pos[1] <= 0:
            self.delta = 0
        
        if pos[3] >= canvas_height:
            self.delta = 0

    
    def moveUp(self, event):
        self.delta = -4

    def moveDown(self, event):
        self.delta = 4

leftpaddle = Paddle(canvas, "orange", 10, 200)
leftpaddle.moveUpDownUsing("<KeyPress -w>","<KeyPress-s>")

rightpaddle = Paddle(canvas, "green", 570, 200)
rightpaddle.moveUpDownUsing("<KeyPress-Up>","<KeyPress-Down>")

leftPaddleScore = 0
rightPaddleScore = 0

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.ball = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.ball, canvas_width/2, canvas_height/2)
        self.deltax = random.choice([-2,2])
        self.deltay = random.choice([-2,2])

    def draw(self):
        global leftPaddleScore, rightPaddleScore
        self.canvas.move(self.ball, self.deltax, self.deltay)
        pos = self.canvas.coords(self.ball)
        if pos[1] <= 0:
            self.deltay = 2

        if pos[3] >= canvas_height:
            self.deltay = -2

        if pos[0] <= 0:
            rightPaddleScore += 1
            canvas.itemconfigure(
                scoring_text,
                text = str(leftPaddleScore) +":"+str(rightPaddleScore)
            )
            self.reset()

        if pos[2] >= canvas_width:
            leftPaddleScore += 1
            canvas.itemconfigure(
                scoring_text,
                text = str(leftPaddleScore) +":"+str(rightPaddleScore)
            )
            self.reset()

        if self.hit_paddle(pos):
            self.deltax = 2

        if self.hit_paddle2(pos):
            self.deltax = -2

    def reset(self):
        self.canvas.coords(self.ball, 290, 240, 310, 260)
        self.deltax = random.choice([-2,2])
        self.dektay = random.choice([-2,2])

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(leftpaddle.paddle)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:

            if pos[0] >= paddle_pos[0] and pos [0] <= paddle_pos[2]:

                return True
            
        return False
    
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(rightpaddle.paddle)

        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
        return False
        
ball = Ball(canvas, "yellow")

def game_loop():
    global leftPaddleScore, rightPaddleScore
    leftpaddle.draw()
    rightpaddle.draw()
    ball.draw()
    if leftPaddleScore == 5 or rightPaddleScore == 5:
        winner = ""
        if leftPaddleScore == 5:
            winner = "Left Player Wins"
        
        else:
            winner = "Right Player Wins"

        messagebox.showinfo("Game Over", winner)
        win.destroy()
        return
    win.after(15, game_loop)

game_loop()
win.mainloop()