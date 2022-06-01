import turtle
turtle.setpos(-600,600)
for i in range(8):
    print(turtle.ycor())
    if i%2 == 0:
        jj = 1
    else:
        jj = 0
    for k in range(8):
        if jj == 1:
            if k%2 == 0:
                j = 1
            else:
                j = 0
            if j == 1:
                turtle.color("red")
            else:
                turtle.color("black")
        else:
            if k%2 == 0:
                j = 1
            else:
                j = 0
            if j == 1:
                turtle.color("black")
            else:
                turtle.color("red")
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(80)
    turtle.setpos(-600, 600-80*(i+1))
