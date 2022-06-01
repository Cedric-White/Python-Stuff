import turtle
import random
leo = turtle.Turtle()
leo.color("Red")
leo.shape("turtle")
leo.setpos(-630,150)
mikey = turtle.Turtle()
mikey.color("Blue")
mikey.shape("turtle")
mikey.setpos(-630,100)
don = turtle.Turtle()
don.color("Green")
don.shape("turtle")
don.setpos(-630,50)
while(leo.xcor() <= 400) and (mikey.xcor() <= 400) and (don.xcor() <= 400):
    leo.forward(random.randint(1,16))
    mikey.forward(random.randint(1,16))
    don.forward(random.randint(1,16))
