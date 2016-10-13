# In this task you will create a program that prints out pascal's triangle (https://upload.wikimedia.org/wikipedia/commons/f/f6/Pascal%27s_triangle_5.svg)
# A user will give input for how many rows they want the triangle printed out to
  # The program will print to the commandline pascal's triangle, formatted the same way as in the image
  
  
  
# Hi - Vincent. This is the finished code. Please check if it is how you wanted it. ~ Saffa
import turtle

tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess.color("red")
tess.pensize(5)


def input():
    times = raw_input("How many rows do you want?:  ")
    return times


def function(my_times):
    x = 0
    y = 0
    dist = 20*int(my_times)
    for i in range(int(my_times)):
        x += 10
        y += 10
        dist -= 20
        # tess.setpos(x, y)
        tess.speed(1)
        tess.fd(int(dist))
        tess.penup()
        tess.setpos(x, y)
        tess.left(90)
        tess.fd(10)
        tess.right(90)
        tess.pendown()


def main():
    #input()
    function(input())
    wn.exitonclick()
main()
