# Your Name: Cedric White 

import turtle, platform

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

#Part 1: cents
#==========================================
# Purpose: Calculates the value of different amounts
# of the four different types of coins in regards to USD 
# Input Parameter(s): Takes four int values; the first
# is for how many quarters, the second for dimes, the
# third for nickels, and the last for pennies. 
# Return Value: The calculation of how ever many
# Quarters, dimes, nickles, and pennies added together.    
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

#Part 2: draw_M
#==========================================
# Purpose: Displays University of Minneasota
# Logo   
# Input Parameter(s): None
#   
# Return Value: None (Doesn't have a return
#statement, but it does print turtle graphics for our Logo)   
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
