from turtle import *

speed(0.001)
left(90)
cell = 40

for i in range(7):
    forward(10 * cell)
    right(120)

penup()
for x in range(11):
    for y in range(11):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()
