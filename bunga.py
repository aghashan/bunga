
import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('#262626')
t.pencolor('#f4f811')
t.speed(100)
col = ('#57f8c8', '#7ababb', '#757c9a', '#f9e02e')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(5)
            t.circle(100+n*20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n % 4])
s.exitonclick()
