import turtle
import random
def rand_color():
    l = ["red", "orange", "yellow", "green", "blue", "purple"]
    return random.choice(l)

class Shape:
    def __init__(self, x=0 , y=0, color="", filled = False):
        self.x = x
        self.y = y
        self.color = color
        self.filled = filled

    def set_color(self, s):
        self.color = s

    def get_color(self):
        return self.color

    def __str__(self):
        return "loc:(" +  str(self.x) + ',' + str(self.y) + ") color:" + self.color

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.penup()

class Circle(Shape):
    def __init__(self, x=0 , y=0, r = 10):
        super().__init__(x, y, rand_color())
        self.radius = r

    def __str__(self):
        return Shape.__str__(self) + " rad:" + str(self.radius)

    def draw(self, turtle):
        turtle.goto(self.x, self.y-self.radius)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        
class Display:
    def __init__(self):
        self.t = turtle.Turtle()
        self.scr = self.t.getscreen()
        self.scr.onclick(self.mouse_event)
        self.scr.listen()
        self.elements = []
        self.t.speed(0)
        self.scr.delay(0)
        self.t.hideturtle()
        self.t.penup()

    def mouse_event(self, x, y):
        r = random.randint(10, 50)
        c = Circle(x, y, r)
        c.draw(self.t)
        
d = Display()
