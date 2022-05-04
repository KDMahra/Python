# importing turtle module
import turtle
  
# Backgroung color
window = turtle.Screen() 
window.bgcolor("orange") 

# number of sides
n = 20
  
# creating instance of turtle
pen = turtle.Turtle()
  
# loop to draw a side
for i in range(n):
    # drawing side of 
    # length i*10
    pen.forward(i * n)
  
    # changing direction of pen 
    # by 144 degree in clockwise
    pen.right(144)
  
# closing the instance
turtle.done()