import turtle as trtl
import random as rand
# set up screen

wn = trtl.Screen()
wn.setup(width=800, height=800)
wn.bgpic("bg.png")
wn.tracer(0)


#snake head
snake_head = trtl.Turtle()
snake_head.penup()
snake_head.goto(0,-45)
snake_head.shapesize(2, 2)
snake_head.shape("square")
snake_head.color("#5A935A")

snake_head.direction = "stop"

segments = []
Step = 20

#food 


food = trtl.Turtle()
food.hideturtle()

wn.addshape("apple.gif")
food.shape("apple.gif")
food.shapesize(0.5, 0.5)
food.penup()

# game over text
game_over = trtl.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.color("white")
game_over.goto(0, 300)




#score
score = 0
score_display = trtl.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-330, 330)
score_display.write("Score: " + str(score), align="left", font=("times new roman", 24, "normal"))




#functions 

def up():
    snake_head.setheading(90)
    
   
def down():
    snake_head.setheading(270)
   

def left():
    snake_head.setheading(180)
   
def right():
    snake_head.setheading(0)
    
def move():
    # record positions (head + all segments) before moving
    positions = [snake_head.position()] + [s.position() for s in segments]

    # move head if inside bounds
    x = snake_head.xcor()
    y = snake_head.ycor()
    if -335 < x < 335 and -320 < y < 270:
        snake_head.speed(3)
        snake_head.forward(Step)

    # move each segment to the previous piece's old position
    for i, seg in enumerate(segments):
        seg.goto(positions[i])

    wn.ontimer(move, 100)
       
def stop():  
    snake_head.forward(0)

def draw_food():
    x2 = rand.randint(-300, 300)
    y2 = rand.randint(-250, 250)
    food.goto(x2, y2)
    food.showturtle()
   

def grow():
    new_seg = trtl.Turtle("square")
    new_seg.color("#5A935A")
    new_seg.shapesize(2, 2)
    new_seg.penup()
    if segments:
        new_seg.goto(segments[-1].position())
    else:
        new_seg.goto(snake_head.position())
    segments.append(new_seg)
    
#key presses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down") 
wn.onkeypress(left, "Left") 
wn.onkeypress(right, "Right")
wn.listen()

# loop
move()

def game_loop():
    global score
    wn.update()

    # game over check
    if snake_head.xcor() > 335 or snake_head.xcor() < -335 or snake_head.ycor() > 270 or snake_head.ycor() < -320:
        stop()
        game_over.write("Game Over", align="center", font=("Arial", 36, "normal"))
        score_display.clear()
        score_display.write("Score: " + str(score), align="left", font=("times new roman", 24, "normal"))
        return

    # spawn food if not visible
    if not food.isvisible():
        draw_food()

    # self collision check
    for segment in segments:    
        if snake_head.distance(segment) < 15:
            stop()
            game_over.write("Game Over", align="center", font=("Arial", 36, "normal"))
            score_display.clear()
            score_display.write("Score: " + str(score), align="left", font=("times new roman", 24, "normal"))
            return


    
    # food collision
    if snake_head.distance(food) < 40:
        score += 10
        score_display.clear()
        grow()
        wn.update()
        
        # hide the food then respawn
        food.hideturtle()
        draw_food()
        score_display.write("Score: " + str(score), align="left", font=("times new roman", 24, "normal"))

    wn.ontimer(game_loop, 100)

# start the game loop and enter the event loop
game_loop()
wn.mainloop()
