# Snake game
Used python package Tkinter to do this game.

<img src="https://user-images.githubusercontent.com/120312056/208252114-20aeccb1-a0bd-4992-a2f1-df2deea6d367.png" alt="image" width="200"/>

## Main features
It uses arrow keys to move and wasd if 2 players mode is selected.

<img src="https://user-images.githubusercontent.com/120312056/208252279-729359a9-beec-4b4d-80da-b2a57ffb5715.png" alt="image1" width="200"/>
<img src="https://user-images.githubusercontent.com/120312056/208252362-0aed3737-865f-4b93-a8a9-a9624bf0672c.png" alt="image1" width="200"/>


## To start:
### pip install
```
pip install tkinter
```
## Application initiate
If you installed tkinter you should start main.py to start this snake game.
```
snake.py
```
## Game Definition
It has 2 modes to play. 
- 1player
: The classic snake game which we played for almost 25 years.
- 2players 
: The 2 player snake game which you necessarily don't need to eat food to win. However, you have to be consistent, creative to defeat other player.
### The necessary conditions to end this game: 
- When you collided into the border line.
- When you collided into your own body.
- When you collided into other player's body.
- 
## Function description
### 1.The main.py file.
It has splash screen to navigate wheter player wants to play single player or multiplayer mode. And then it calls the member function to call single or multiplayer by button input.
```
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
```
 
### 2. The snake.py file
This is the file which single player mode is written. As I said earlier I used tkinter library to create window and random library to get random int. 
```python:
from tkinter import *
import random
```
I defined these files to create constants. But python does not support constants so I marked them by upper case letters. And init function to call this whole file.

```python:
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 25
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
direction = 'down'
score = 0
```
Snake class is the class to initialize the head postition and store the variables which is needed to draw body later.

```python:
    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0,BODY_PARTS):
                self.coordinates.append([0,0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE,    fill=SNAKE_COLOR, tag= "snake")
                self.squares.append(square)
```
Food class creates the food in random position in the field.

```python:
    class Food:
        def __init__(self):
            x = random.randint(0,(GAME_WIDTH / SPACE_SIZE)-1)*SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x,y]

            canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

```
This function takes the keyboard input as new direction and change the direction when the input is not opposite of the last direction input. Ex: you can not turn right when you head is headed into the left.

```python:
    def change_direction(new_direction):
        global direction
        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction
```
This function checks the head is collided into the border or it's body (Additionally, with other person's body).

```python:
 def check_collision(snake):
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH:
            print("Game Over!!!")
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            print("Game Over!!!")
            return True
        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print("Game Over!!!")
                return True
        return False

```
This function deletes all the things in the field and prints "game over" when called.

```python:
    def game_over():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                           font=('consolas',70),text = "GAME OVER\n Score:{}".format(score),fill="red",tag="Gameover")

```
This function runs the game. It takes 2 (3 in 2 player mode) parameter which is food and the snake. Firstly, it moves the head according to the direction. And draws the body rectangles. Next, it checks the head position and the food position to decide either delets the last part or keep it and increment the score. Lastly, it checks that the game is over or not.  

```python:
    def game(snake, food):
        x, y = snake.coordinates[0]
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x+=SPACE_SIZE
        snake.coordinates.insert(0,(x,y))
        square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
        snake.squares.insert(0, square)
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        if check_collision(snake):
            game_over()
        else:
            window.after(SPEED, game, snake, food)

```
Lastly, The other things. Such as, draw the window, label to store text, keyboard input, object creation, positioning the window and calling the game function.

```python:
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

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    game(snake, food)
```
## Conclusion:
Firstly, I regrets that I could do so much more to this game if I started earlier. Like invisibility, timer, more urban style, background, more possibilities to play etc. I finally understand my professor's lecture that talks about if I give you deadline at 12/15 you start at 12/8. However, I think that I will continue this game until I fulfill my goal as this game's creator because it is the OSS. Maybe this Conlusion will be deleted. I had to start from the scratch because I wanted that way and decided not to copy someone's code. So I needed to learn python addition to what I know and learn Tkinter from the start. So, I think this was very fun project to do. 
