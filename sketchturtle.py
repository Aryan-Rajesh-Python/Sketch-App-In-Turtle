import turtle
from turtle import Turtle,Screen
tortoise=Turtle()
screen=Screen()
def move_forward():
    tortoise.forward(100)
def move_backward():
    tortoise.backward(100)
def turn_left():
    tortoise.left(100)
def turn_right():
    tortoise.right(100)
def clear():
    tortoise.clear()
    tortoise.penup()
    tortoise.home()
    tortoise.pendown()
screen.listen()
screen.onkey(key="f",fun=move_forward)
screen.onkey(key="b",fun=move_backward)
screen.onkey(key="l",fun=turn_left)
screen.onkey(key="r",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()