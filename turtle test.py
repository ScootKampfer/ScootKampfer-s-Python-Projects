from turtle import *
import time
n = 0
m = 0
p = 0

shape('turtle')

#we are making an among us drawing, which is a bit sus

forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(65)

left(90)
forward(10)

while m < 181:

    forward(0.17452777777)
    right(1)
    m = m + 1

forward(20)

while p < 181:

    forward(0.17452777777)
    right(1)
    p = p + 1

forward(20)
m = 0

while m < 181:

    forward(0.17452777777)
    right(1)
    m = m + 1

forward(10)

left(90)


forward(20)

while n < 181:

    forward(0.78539816339)
    left(1)
    n = n + 1
    
forward(100)
back(50)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(90)

time.sleep(5)

quit()