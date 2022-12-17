from tkinter import *
from tkinter.font import Font
import snake as snake
import Snake2 as snake2

splash_window = Tk()
purisafont = Font(family="purisa", size=50, weight="bold")
splash_window.geometry("700x700")
splash_window.resizable(False,False)
splash_window.title("Snake Game")
bg = PhotoImage(file = "resources/SnakeScreen.png")
canvas = Canvas(splash_window, width = 700, height = 700)
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.image = bg
canvas.create_rectangle(80,100, 600,300,fill = "#95b305",outline = "#95b305", stipple='gray50')
canvas.create_text(350,200, text="Welcome to the \nsnake game",font = purisafont,fill="black")

playerOne = Button(splash_window,
                   text=" 1  player",
                   font=("concolas",30),
                   command=(lambda:snake.init(splash_window)),
                   bg="#00FF00"
                   )

playerTwo = Button(splash_window,
                   text="2 players",
                   font=("concolas",30),
                   command= lambda:snake2.init(splash_window),
                   bg = "#00FF00")
playerOne_window = canvas.create_window(270, 450, anchor ="nw", window=playerOne)
playerTwo_window = canvas.create_window(270, 560, anchor ="nw", window=playerTwo)
canvas.pack(fill = "both", expand = True)

splash_window.mainloop()