def mul(a,b):
    i = 0
    c = 0 
    while i < a:
        c += b 
        i += 1
    return c
import turtle

def expo(a,b):
    i = 0
    c = 0
    if b == 0:
            return 1
    while i < b-1:
        if i < 1:
            c = mul(a,a)
        else:
            c = mul(c,a)
        i+=1
    return c
def div27(num):
    for i in range(2,8):
        if num % i == 0:
            return True
    return False

sqrt3 = 3**0.5
leo = turtle.Turtle()
leo.color("blue")
leo.shape("arrow")
mikey = turtle.Turtle()
mikey.color("orange")
mikey.shape("circle")
don = turtle.Turtle()
don.color("purple")
don.shape("square")
raph = turtle.Turtle()
raph.color("red")
raph.shape("turtle")
leo.forward(50*sqrt3)
mikey.setpos(-50*sqrt3,0)
don.circle(50)
leo.left(120)
leo.forward(100*sqrt3)
mikey.setpos(0,150)
raph.left(90)
raph.forward(150)
