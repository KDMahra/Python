import turtle

#window screen for output
screen = turtle.Screen()

#background of screen
screen.bgcolor("white")

# Defining a turtle Instance
pen = turtle.Turtle()

# initially penup()
pen.penup()
pen.goto(0,100)
pen.pendown()

# Orange Rectangle
pen.color("orange")
pen.begin_fill()
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.end_fill()

pen.left(90)
pen.forward(50)
pen.left(90)

#Green Rectangle
pen.color("green")
pen.begin_fill()
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.end_fill()

#pole
pen.left(90)
pen.forward(200)



#to hold the output window screen
turtle.done()