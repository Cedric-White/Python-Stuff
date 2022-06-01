import turtle
import random
def sum_list(vals):
    if len(vals) == 0:
        return 0
    else:
        print("At this step we do",vals[0], "+ sum of",vals[1:])
        return vals[0] + sum_list(vals[1:])

def reverse_string(st):
    if len(st) == 1:
        return st
    else:
        return st[len(st)-1] + reverse_string(st[:len(st)-1])

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def print_f():
    for i in range(20):
        print(fibonacci(i))
def tree(t, trunk_length):
    if trunk_length < 5:
        return
    else:
        r = random.randint(15, 45)
        l = random.randint(12,18)
        t.forward(trunk_length)
        t.right(r)
        tree(t, trunk_length-l)
        t.left(r*2)
        tree(t, trunk_length-l)
        t.right(r)
        t.backward(trunk_length)
#tree_turtle = turtle.Turtle()
#tree_turtle.left(90)
#tree_turtle.speed(0)
#tree(tree_turtle,100)
def flat_square(ls):
    #print(ls)
    if type(ls) == list:
        if len(ls) == 0:
            return []
        if len(ls) == 1:
            ls = ls[0]
            return flat_square(ls)  
    if type(ls) == int:
        return [ls] 
    else:
        return flat_square(ls[0]) + flat_square(ls[1:])

