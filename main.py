import tkinter
from tkinter import *
import random

GAME = 0
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 1000
SPACE_SIZE = 50
BODY_PARTS = 1
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOR = "#000000"
SNAKE1_COLOUR = "#00FF00"
SNAKE2_COLOUR = "#0000FF"

score = 0
direction1 = 'down'
direction2 = 'down'
splash_window = Tk()

def Main_window(a):
    splash_window.destroy()

    class Snake1:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])
            for x1, y1 in self.coordinates:
                square1 = canvas.create_rectangle(x1, y1, x1 + SPACE_SIZE, y1 + SPACE_SIZE, fill=SNAKE1_COLOUR,
                                                  tag="snake1")
                self.squares.append(square1)

    class Snake2:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([500, 500])
            for x2, y2 in self.coordinates:
                square2 = canvas.create_rectangle(x2, y2, x2 + SPACE_SIZE, y2 + SPACE_SIZE, fill=SNAKE2_COLOUR,
                                                  tag="snake2")
                self.squares.append(square2)

    class Food:
        def __init__(self):
            x3 = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y3 = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x3, y3]
            canvas.create_oval(x3, y3, x3 + SPACE_SIZE, y3 + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

    def next_turn(snake1, snake2, food):
        x1, y1 = snake1.coordinates[0]
        x2, y2 = snake2.coordinates[0]

        if direction1 == 'up':
            y1 -= SPACE_SIZE
        elif direction1 == 'down':
            y1 += SPACE_SIZE
        elif direction1 == 'left':
            x1 -= SPACE_SIZE
        elif direction1 == 'right':
            x1 += SPACE_SIZE

        if direction2 == 'up1':
            y2 -= SPACE_SIZE
        elif direction2 == 'down1':
            y2 += SPACE_SIZE
        elif direction2 == 'left1':
            x2 -= SPACE_SIZE
        elif direction2 == 'right1':
            x2 += SPACE_SIZE

        snake1.coordinates.insert(0, (x1, y1))
        square1 = canvas.create_rectangle(x1, y1, x1 + SPACE_SIZE, y1 + SPACE_SIZE, fill=SNAKE1_COLOUR)
        snake1.squares.insert(0, square1)

        snake2.coordinates.insert(0, (x, y))
        square2 = canvas.create_rectangle(x2, y2, x2 + SPACE_SIZE, y2 + SPACE_SIZE, fill=SNAKE2_COLOUR)
        snake2.squares.insert(0, square2)

        if x1 == food.coordinates[0] and y1 == food.coordinates[1]:
            global score1
            score1 += 1
            #label1.config(text="Score: {}".format(score1))
            canvas.delete("food")
            food = Food()
        else:
            del snake1.coordinates[-1]
            canvas.delete(snake1.squares[-1])
            del snake1.squares[-1]

        if check_collision(snake1):
            Player2Lose()
        else:
            window.after(SPEED, next_turn, snake1, snake2, food)
        if check_collision(snake2):
            Player1Lose()
        else:
            window.after(SPEED, next_turn, snake1, snake2, food)

        if x2 == food.coordinates[0] and y2 == food.coordinates[1]:
            global score2
            score2 += 1
            #label2.config(text="Score2: {}".format(score2))
            canvas.delete("food")
            food = Food()
        else:
            del snake2.coordinates[-1]
            canvas.delete(snake2.squares[-1])
            del snake2.squares[-1]
        if check_collision(snake2):
            Player2Lose()
        else:
            window.after(SPEED, next_turn, snake1, snake2, food)

    def change_direction1(new_direction1):
        global direction1

        if new_direction1 == 'left':
            if direction1 != 'right':
                direction1 = new_direction1
        if new_direction1 == 'right':
            if direction1 != 'left':
                direction1 = new_direction1
        if new_direction1 == 'up':
            if direction1 != 'down':
                direction1 = new_direction1
        if new_direction1 == 'down':
            if direction1 != 'up':
                direction1 = new_direction1

    def change_direction2(new_direction2):
        global direction2

        if new_direction2 == 'left1':
            if direction2 != 'right1':
                direction2 = new_direction2
        if new_direction2 == 'right1':
            if direction2 != 'left1':
                direction2 = new_direction2
        if new_direction2 == 'up1':
            if direction2 != 'down1':
                direction2 = new_direction2
        if new_direction2 == 'down1':
            if direction2 != 'up1':
                direction2 = new_direction2

    def check_collision(snake1, snake2):
        x1, y1 = snake1.coordinates[0]
        x2, y2 = snake2.coordinates[0]
        state = 0

        if x1 < 0 or x1 >= GAME_WIDTH:
            print("Game Over!!!")
            state = 1
            return state
        elif y1 < 0 or y1 >= GAME_HEIGHT:
            print("Game Over!!!")
            state = 1
            return state
        if x2 < 0 or x2 >= GAME_WIDTH:
            print("Game Over!!!")
            state = 2
            return state
        elif y2 < 0 or y2 >= GAME_HEIGHT:
            print("Game Over!!!")
            state = 2
            return state
        for body_part in snake1.coordinates[1:]:
            if x2 == body_part[0] and y2 == body_part[1]:
                print("Game Over!!!")
                state = 2
                return state
        for body_part2 in snake2.coordinates[1:]:
            if x1 == body_part[0] and y1 == body_part2[1]:
                print("Game Over!!!")
                state = 1
                return state

        return state

    def Player1Lose():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('consolas', 50), text="Player 2 Victory!!!", fill="red", tag="Player2Won")
    def Player2Lose():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('consolas', 50), text="Player 1 Victory!!!", fill="red", tag="Player1Won")
    window = Tk()
    window.title("Snake Game")
    window.resizable(False,False)

    label = Label(window,text = "Score:{}".format(score),font = ('consolas',40))
    label.pack()

    canvas = Canvas(window,bg = BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction1('left'))
    window.bind('<Right>', lambda event: change_direction1('right'))
    window.bind('<Up>', lambda event: change_direction1('up'))
    window.bind('<Down>', lambda event: change_direction1('down'))

    window.bind('<a>', lambda event: change_direction2('left1'))
    window.bind('<d>', lambda event: change_direction2('right1'))
    window.bind('<w>', lambda event: change_direction2('up1'))
    window.bind('<s>', lambda event: change_direction2('down1'))

    if a == 1:
        snake1 = Snake1()
        food = Food()
        next_turn(snake1, food)
    elif a == 2:
        snake1 = Snake1()
        food = Food()
        snake2 = Snake2()
        next_turn(snake1, snake2, food)

def splash_screen():
    splash_window.geometry("700x700")
    splash_window.configure(bg="black")
    splash_label = Label(splash_window,text="Welcome to \nClassic snake game!!",font=("consolas",40),fg= "blue")
    splash_label.configure(bg="black")
    splash_label.pack(pady= 20)
    playerOne = Button(splash_window,
                       text="1 player",
                       command=one_player,
                       font=("consolas",30),
                       fg="#00FF00",
                       bg="black",
                       activebackground="black",
                       activeforeground="#00FF00",
                       )
    playerOne.pack()
    playerTwo = Button(splash_window,
                       text="2 players",
                       command=two_players,
                       font=("consolas", 30),
                       fg="#00FF00",
                       bg="black",
                       activebackground="black",
                       activeforeground="#00FF00",
                       )
    playerTwo.pack()

def one_player():
    GAME = 1
    Main_window(GAME)

def two_players():
    GAME = 2
    Main_window(2)

def howToPlay():

    play = Tk()
    play.configure(bg="black")

    playL = Label(play, text="The first one who collides into border or\n "
                             "opponent's body will lose.\n"
                             "\n"
                             "If heads are collide into each other that will be tie. \n"
                             "The random spawning food can make your\n "
                             "body more longer and more dangerous",
                  font=("concolas",40),fill="red")


    playL.pack(pady=20)



splash_screen()
mainloop()