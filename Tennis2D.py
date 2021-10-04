import turtle
from tkinter import *

start = Tk()
start.geometry("1280x720")
start.title("Tennis")

def login():

    global bgimg, startgame, exit
    bgimg = PhotoImage(file='Images/tennisball 2.png')
    Label(start, image=bgimg).place(x=0, y=0)

    startgame = PhotoImage(file='Images/START GAME.png')
    start_button = Button(start, image=startgame, bg="#AFC13C", bd=0, activebackground="#AFC13C", command=startbtn)
    start_button.place(x=66, y=532)

    exit = PhotoImage(file='Images/EXIT.png')
    exit_button = Button(start, image=exit, bg="#AFC13C", bd=0, activebackground="#AFC13C", command=exitbtn)
    exit_button.place(x=66, y=605)

def exitbtn():
    start.quit()

def startbtn():

        # creating a window
        WIN = turtle.Screen()

        # giving it a title
        WIN.title("TENNIS")

        # customising the window
        WIN.bgcolor("black")
        WIN.setup(width=800, height=600)
        WIN.bgpic('Images/court.gif')

        # stopping window from updating, allowing game to speed up
        WIN.tracer(0)

        # adjusting ball's speed
        score_1 = 0
        score_2 = 0

        # adding and adjusting player 1
        player1 = turtle.Turtle()
        player1.speed(0)
        player1.shape("square")
        player1.color("red")
        player1.shapesize(stretch_wid=5, stretch_len=1)

        # disabling turtle from drawing lines when they move
        player1.penup()

        # starting point of player 1
        player1.goto(-350, 0)

        # adding player 2
        player2 = turtle.Turtle()
        player2.speed(0)
        player2.shape("square")
        player2.color("blue")
        player2.shapesize(stretch_wid=5, stretch_len=1)

        # disabling turtle from drawing lines when they move
        player2.penup()

        # starting point of player 2
        player2.goto(350, 0)

        # adding ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("orange")

        # disabling turtle from drawing lines when they move
        ball.penup()

        # starting point of ball
        ball.goto(0, 0)

        # adjusting ball's movement speed
        ball.x = 0.7
        ball.y = -0.7

        # creating scoring system
        scr = turtle.Turtle()
        scr.speed(0)
        scr.color("black")
        scr.penup()
        scr.hideturtle()
        scr.goto(0, 260)
        scr.write("Player 1: 0               Player 2: 0", align="center", font=("Arial", 15, "italic"))

        # adding movement to players
        def player1_UP():
            Yaxis = player1.ycor()
            Yaxis += 20
            player1.sety(Yaxis)

        def player1_DOWN():
            Yaxis = player1.ycor()
            Yaxis -= 20
            player1.sety(Yaxis)

        def player2_UP():
            Yaxis = player2.ycor()
            Yaxis += 20
            player2.sety(Yaxis)

        def player2_DOWN():
            Yaxis = player2.ycor()
            Yaxis -= 20
            player2.sety(Yaxis)

        # assigning keys for game
        WIN.listen()

        WIN.onkeypress(player1_UP, "w")
        WIN.onkeypress(player1_DOWN, "s")

        WIN.onkeypress(player2_UP, "Up")
        WIN.onkeypress(player2_DOWN, "Down")

        # main loop for game
        while True:
            WIN.update()

            # moving the ball
            ball.setx(ball.xcor() + ball.x)
            ball.sety(ball.ycor() + ball.y)

            # adding border so that ball can bounce
            if ball.ycor() > 290:
                ball.sety(290)
                ball.y *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.y *= -1

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.x *= -1
                score_1 += 1
                scr.clear()
                scr.write("Player 1: {}               Player 2: {}".format(score_1, score_2), align="center",
                          font=("Arial", 15, "italic"))

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.x *= -1
                score_2 += 1
                scr.clear()
                scr.write("Player 1: {}               Player 2: {}".format(score_1, score_2), align="center",
                          font=("Arial", 15, "italic"))

            # ball and player's contact
            if (ball.xcor() > 340 and ball.xcor() < 350) and (
                    ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
                ball.setx(340)
                ball.x *= -1

            if (ball.xcor() < -340 and ball.xcor() > -350) and (
                    ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
                ball.setx(-340)
                ball.x *= -1

login()
start.mainloop()