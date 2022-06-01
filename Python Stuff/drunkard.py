import random
import math
import turtle
def drunkards_walk():
    i = 0
    steps = 0
    while True:
        turtle.delay(0)
        turtle.speed(0)
        turtle.forward(30)
        steps += 1
        r = random.randint(1, 4)
        if(r == 1):
            turtle.left(0)
        elif(r == 2):
            turtle.left(90)
        elif(r == 3):
            turtle.left(180)
        elif(r == 4):
            turtle.left(270)
        i += 1
        if((turtle.xcor() > 300) or (turtle.xcor() < -300)):
            return steps
        elif((turtle.ycor() > 300) or (turtle.ycor() < -300)):
            return steps
        
