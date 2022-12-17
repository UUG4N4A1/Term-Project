from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 25
BODY_PARTS = 5
SNAKE_COLOR1 = "#00FF00"
SNAKE_COLOR2 = "#0000FF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

score1 = 0
score2 = 0
direction1 = 'down'
direction2 = 'up1'

def init(sc):
    sc.destroy()
    class Snake1:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR1, tag="snake1")
                self.squares.append(square)

    class Snake2:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([700 - SPACE_SIZE, 700 - SPACE_SIZE])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR2, tag="snake2")
                self.squares.append(square)


    class Food:
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


    def game(snake1, food, snake2):
        x1, y1 = snake1.coordinates[0]
        x2, y2 = snake2.coordinates[0]

        if direction1 == "up":
            y1 -= SPACE_SIZE

        elif direction1 == "down":
            y1 += SPACE_SIZE

        elif direction1 == "left":
            x1 -= SPACE_SIZE

        elif direction1 == "right":
            x1 += SPACE_SIZE

        if direction2 == "up1":
            y2 -= SPACE_SIZE

        elif direction2 == "down1":
            y2 += SPACE_SIZE

        elif direction2 == "left1":
            x2 -= SPACE_SIZE

        elif direction2 == "right1":
            x2 += SPACE_SIZE
        # DRAWING BODY OF SNAKES
        snake1.coordinates.insert(0, (x1, y1))

        square1 = canvas.create_rectangle(x1, y1, x1 + SPACE_SIZE, y1 + SPACE_SIZE, fill=SNAKE_COLOR1)

        snake1.squares.insert(0, square1)

        snake2.coordinates.insert(0, (x2, y2))

        square2 = canvas.create_rectangle(x2, y2, x2 + SPACE_SIZE, y2 + SPACE_SIZE, fill=SNAKE_COLOR2)

        snake2.squares.insert(0, square2)
        global score1
        global score2
        if x1 == food.coordinates[0] and y1 == food.coordinates[1]:


            score1 += 1

            label.config(text="Score1:{0}    Score2:{1}".format(score1, score2).format(score1))
            canvas.delete("food")

            food = Food()
        else:
            del snake1.coordinates[-1]

            canvas.delete(snake1.squares[-1])

            del snake1.squares[-1]

        if x2 == food.coordinates[0] and y2 == food.coordinates[1]:

            score2 += 1

            label.config(text="Score1:{0}     Score2:{1}".format(score1,score2).format(score2))
            canvas.delete("food")

            food = Food()

        else:
            del snake2.coordinates[-1]

            canvas.delete(snake2.squares[-1])

            del snake2.squares[-1]

        if check_collision(snake1,snake2) == 1:
            Player1Loses()
        elif check_collision(snake1, snake2) == 2:
            Player2Loses()
        else:
            window.after(SPEED, game, snake1, food, snake2)


    def change_direction1(new_direction1):
        global direction1

        if new_direction1 == 'left':
            if direction1 != 'right':
                direction1 = new_direction1
        elif new_direction1 == 'right':
            if direction1 != 'left':
                direction1 = new_direction1
        elif new_direction1 == 'up':
            if direction1 != 'down':
                direction1 = new_direction1
        elif new_direction1 == 'down':
            if direction1 != 'up':
                direction1 = new_direction1


    def change_direction2(new_direction2):
        global direction2

        if new_direction2 == 'left1':
            if direction2 != 'right1':
                direction2 = new_direction2
        elif new_direction2 == 'right1':
            if direction2 != 'left1':
                direction2 = new_direction2
        elif new_direction2 == 'up1':
            if direction2 != 'down1':
                direction2 = new_direction2
        elif new_direction2 == 'down1':
            if direction2 != 'up1':
                direction2 = new_direction2


    def check_collision(snake1, snake2):
        x1, y1 = snake1.coordinates[0]
        x2, y2 = snake2.coordinates[0]
        if x1 < 0 or x1 >= GAME_WIDTH:
            print("Game Over  1!!!")
            return 1
        elif y1 < 0 or y1 >= GAME_HEIGHT:
            print("Game Over  1!!!")
            return 1
        if x2 < 0 or x2 >= GAME_WIDTH:
            print("Game Over  2!!!")
            return 2
        elif y2 < 0 or y2 >= GAME_HEIGHT:
            print("Game Over  2!!!")
            return 2
        for body_part in snake1.coordinates[1:]:
            if x1 == body_part[0] and y1 == body_part[1]:
                print("Game Over  2!!!")
                return 1
        for body_part in snake2.coordinates[1:]:
            if x2 == body_part[0] and y2 == body_part[1]:
                print("Game Over  2!!!")
                return 2

        for body_part in snake1.coordinates[1:]:
            if x2 == body_part[0] and y2 == body_part[1]:
                print("Game Over  2!!!")
                return 2
        for body_part in snake2.coordinates[1:]:
            if x1 == body_part[0] and y1 == body_part[1]:
                print("Game Over  1!!!")
                return 1
        return False


    def Player1Loses():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('consolas', 70), text="Player 1 Lost\n Score : {}".format(score1), fill="red", tag="Gameover")
    def Player2Loses():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('consolas', 70), text= "Player 2 Lost\n Score : {}".format(score2), fill="red", tag="Gameover")


    window = Tk()
    window.title("Snake Game")
    window.resizable(False, False)



    label = Label(window, text="Score1:{0}    Score2 = {1}".format(score1,score2), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction1('left'))
    window.bind('<Right>', lambda event: change_direction1('right'))
    window.bind('<Up>', lambda event: change_direction1('up'))
    window.bind('<Down>', lambda event: change_direction1('down'))

    window.bind('<a>', lambda event: change_direction2('left1'))
    window.bind('<d>', lambda event: change_direction2('right1'))
    window.bind('<w>', lambda event: change_direction2('up1'))
    window.bind('<s>', lambda event: change_direction2('down1'))

    snake1 = Snake1()
    food = Food()
    snake2 = Snake2()


    game(snake1, food, snake2)

    window.mainloop()
