#P4LAB2a Assignment
#CTI-110
#Catherine Adam
#3/30/2022
#
#Using turle graphics and a loop, write a program that draws both
#a triangle and a square.


from turtle import *

shape('square')
for i in range(4):
    left(90)
    forward(150)


shape('triangle')
for i in range(3):
    forward(150)
    left(120)

done()
