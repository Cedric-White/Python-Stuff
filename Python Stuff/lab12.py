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
        self.r = r

    def __str__(self):
        return Shape.__str__(self) + " rad:" + str(self.r)

    def draw(self, turtle):
        turtle.goto(self.x, self.y-self.r)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.r)
        turtle.end_fill()

    def is_in(self, x, y):
        d = (x-self.x)**2 + (y-self.y)**2
        R = self.r**2
        if d <= R:
            return True
        else:
            return False
        
class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, rand_color())
        self.w = w
        self.h = h

    def __str__(self):
        return Shape.__str__(self) + " Width and Height:" + str(self.w) + ' ' + str(self.h)

    def draw(self, turtle):
        turtle.goto(self.x, self.y)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.h)
            turtle.left(90)
            turtle.forward(self.w)
            turtle.left(90)
        turtle.end_fill()

    def is_in(self, x, y):
        if (x >= self.x) and (x <= (self.x+self.w)) and (y >= self.y) and (y <= (self.y+self.h)):
            return True
        else:
            return False
    
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
        self.elements = []

    def mouse_event(self, x, y):
        removed = False
        num = random.randint(1,2)
        for i in self.elements:
            if i.is_in(x, y):
                self.remove(i)
                removed = True
        if removed == False:      
            if num == 1:
                ra = random.randint(10, 50)
                c = Circle(x, y, ra)
                self.add(c)
                    
            if num == 2:
                R = random.randint(20, 70)
                RR = random.randint(20, 70)
                r = Rectangle(x,y,R, RR)
                self.add(r)




    def add(self, shape):
        self.elements.append(shape)
        shape.draw(self.t)
        
    def remove(self, shape):
        self.elements.remove(shape)
        self.t.clear()
        for i in self.elements:
            i.draw(self.t)

class Button(Rectangle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, rand_color())
        self.label = "button"

    def handler()
        pass
    def draw()
        pass
    

d = Display()
c = Circle(100,10, 50)
c2 = Circle(-15, 15, 30)
c3 = Circle(50, 20, 20)
r = Rectangle(100, 100, 50, 80)
d.add(c)
d.add(c2)
d.add(c3)
d.add(r)
