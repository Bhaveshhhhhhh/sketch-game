from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)
screen = Screen()

def move_forwd():
    tim.forward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def move_back():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwd)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="x", fun=clear)
screen.exitonclick()