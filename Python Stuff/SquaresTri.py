import math
import turtle
def draw_square(length, num):
    i = 0
    while i < 4:
        turtle.forward(length)
        turtle.left(90)
        turtle.speed(0)
        i += 1
    turtle.left(num)
    
def draw_triangle(length, num):
    i = 0
    while i < 3:
        turtle.forward(length)
        turtle.left(120)
        turtle.speed(0)
        i += 1
    turtle.left(num)
num = int(input("Enter the number of shapes: "))
c = input("Enter shape type (S or s for square, T or t for triangle): ")
if((c == 'S') or (c == 's')):
    j = 0
    right = 0
    while j < num:
        #print(j, num)
        right = 360/num
        draw_square(100, right)
        j += 1
elif((c == 'T') or (c == 't')):
    j = 0
    right = 0
    while j < num:
        #print(j, num)
        right = 360/num
        draw_triangle(100, right)
        j += 1
else:
    print("Illegal shape type entered: ", c)


        
