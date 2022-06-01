import turtle
def diagonal_fives():
    ls = [0,0,0,0]  
    count = 0
    x = 5
    mat = []
    for i in range(4):
        ls=[0,0,0,0]
        mat.append(ls)
        mat[i][count] = x
        count+=1
    print(mat)

def dist(p1, p2):
    x = p1[0]
    y = p1[1]
    xx = p2[0]
    yy = p2[1]
    dist = ((xx-x)**2 + (yy-y)**2)**.5
    return dist

def shortest_dist(ls):
    short = 100
    for i in range(len(ls)):
        for n in range(i+1,len(ls)):
            if short > dist(ls[i],ls[n]):
                short = dist(ls[i],ls[n])
    return short

def draw_grid(grid):
    true = turtle.Turtle()
    true.speed(0)
    turtle.setworldcoordinates(-1, -1, 10, 10)
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n] == 0:
                true.color("white")
            else:
                true.color("black")
            for s in range(4):
                turtle.forward(10)
                turtle.left(90)
                
    


