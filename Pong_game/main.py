import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("light blue")
window.setup(width=1000, height=600)
window.tracer(0)

# Score
player1 = 0
player2 = 0

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=0.5)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.write("Player 1", align="center", font=("Arial", 12, "normal"))

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=0.5)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.write("Player 2", align="center", font=("Arial", 12, "normal"))

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 20, "normal"))


# Functions
def paddleAUp():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddleADown():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddleBUp():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddleBDown():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# controls
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")

# Main game loop
while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle and ball collisions
    if ball.xcor() < -340 and paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 30:
        ball.dx *= -1

    elif ball.xcor() > 340 and paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 30:
        ball.dx *= -1

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        player1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player1, player2), align="center", font=("Arial", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        player2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player1, player2), align="center", font=("Arial", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


