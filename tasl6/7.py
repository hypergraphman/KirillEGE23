from turtle import *


def move(a, b):
    global x, y
    x += a * cell
    y += b * cell
    goto(x, y)


speed(0.001)
cell = 5
x = 0
y = 0

for i in range(15):
    move(10, 10)
    move(3, -6)
    move(-9, 3)

penup()
for x in range(15):
    for y in range(11):
        goto(x * cell, y * cell)
        dot(2, 'red')

done()
