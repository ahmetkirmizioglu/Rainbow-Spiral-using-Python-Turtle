import turtle
turtle.title("Ahmet")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.setup(480, 480, startx=60, starty=70)
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(80):
    t.pencolor(colors[x%6])
    t.width(x//10 + 2)
    t.forward(x)
    t.left(x//100 + 30)
    t.speed(x*5)
turtle.done()