# Simple pong game in Python 3 
#Made by Magsud Hasanov with the help of freeCodeCamp.org


# packages

import turtle
import winsound

# window of game

window = turtle.Screen()                            # creating object
window.title("Pong game by Magsud Hasanov")         # name of the window
window.bgcolor("black")                             # background color  
window.setup(width=800, height=600)                 # dimensions of window
window.tracer(0)                                    # stop updating window (increases the productivity)

# Score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()                          # creating object
paddle_a.speed(0)                                   # speed of animation (maximum speed)
paddle_a.shape("square")                            # shape of the paddle (square)
paddle_a.color("white")                             # color of the paddle (white)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # streching the standard square to make it rectangular
paddle_a.penup()                                    # not to draw a line (for turtle package)
paddle_a.goto(-350, 0)                              # starting coordinates of paddle_a (x,y)

# Paddle B

paddle_b = turtle.Turtle()                          # creating object
paddle_b.speed(0)                                   # speed of animation (maximum speed)
paddle_b.shape("square")                            # shape of the paddle (square)
paddle_b.color("white")                             # color of the paddle (white)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    # streching the standard square to make it rectangular
paddle_b.penup()                                    # not to draw a line (for turtle package)
paddle_b.goto(350, 0)                               # starting coordinates of paddle_b (x,y)



# Ball

ball = turtle.Turtle()                          # creating object
ball.speed(0)                                   # speed of animation (maximum speed)
ball.shape("square")                            # shape of the ball (square)
ball.color("white")                             # color of the ball (white)
ball.penup()                                    # not to draw a line (for turtle package)
ball.goto(0, 0)                                 # starting coordinates of ball, center (x,y)
ball.dx = 0.1                                  # speed of changing in x direction                                     
ball.dy = 0.1                                  # speed of changing in y direction

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions

def paddle_a_up():                              # paddle_a goes up
    y = paddle_a.ycor()                         # ycor() returns y coordinate (turtle package)
    y += 20                                     # size of the step
    paddle_a.sety(y)                            # after new y is given we set coordinates of paddle with new y


def paddle_a_down():                            # paddle_a goes down
    y = paddle_a.ycor()                         # ycor() returns y coordinate (turtle package)
    y -= 20                                     # size of the step
    paddle_a.sety(y)


def paddle_b_up():                              # paddle_a goes up
    y = paddle_b.ycor()                         # ycor() returns y coordinate (turtle package)
    y += 20                                     # size of the step
    paddle_b.sety(y)                            # after new y is given we set coordinates of paddle with new y


def paddle_b_down():                            # paddle_a goes down
    y = paddle_b.ycor()                         # ycor() returns y coordinate (turtle package)
    y -= 20                                     # size of the step
    paddle_b.sety(y)

# Keyboard binding
window.listen()                                 # the window "listens" our keyboard
window.onkeypress(paddle_a_up, "w")             # when pressing "w" on keyboard, it calls this function (case sensitive)
window.onkeypress(paddle_a_down, "s")           # when pressing "s" on keyboard, it calls this function (case sensitive)

window.onkeypress(paddle_b_up, "Up")            # when pressing "Up arrow key" on keyboard, it calls this function (case sensitive)
window.onkeypress(paddle_b_down, "Down")        # when pressing "Down arrow key" on keyboard, it calls this function (case sensitive)


# Main game loop

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))   

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))   
 

    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
