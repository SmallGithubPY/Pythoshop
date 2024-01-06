#Importing some stuff... :)
from turtle import Turtle
from turtle import Screen
import turtle as t

#Defining Pythoshop and buttons
pythoshop = Turtle()
drawbtn = Turtle()
penhide = Turtle()
penshow = Turtle()
roleft = Turtle()

#Making some code
def draw(x,y):
    pythoshop.forward(10)
    
def pznhide(x,y):
    pythoshop.pencolor("white")
    
def pznshow(x,y):
    pythoshop.pencolor("black")
    
def rolex(x,y):
    pythoshop.left(90)
    
pythoshop.shapesize(1)
pythoshop.pensize(10)
drawbtn.shapesize(10)
drawbtn.shape("circle")
drawbtn.color("blue")
drawbtn.pencolor("white")
drawbtn.right(90)
drawbtn.forward(900)
drawbtn.right(90)
drawbtn.forward(300)
drawbtn.onclick(draw)
penhide.shapesize(10)
penhide.shape("circle")
penhide.pencolor("white")
penhide.right(90)
penhide.forward(900)
penhide.onclick(pznhide)
penshow.shapesize(10)
penshow.shape("circle")
penshow.color("green")
penshow.pencolor("white")
penshow.right(90)
penshow.forward(900)
penshow.left(90)
penshow.forward(300)
penshow.onclick(pznshow)
roleft.shapesize(10)
roleft.shape("circle")
roleft.color("pink")
roleft.pencolor("white")
roleft.left(90)
roleft.forward(900)
roleft.right(90)
roleft.onclick(rolex)

#Screen Loop
t.done()