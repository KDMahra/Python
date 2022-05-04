
# Hexagon
import turtle
window = turtle.Screen() 
window.bgcolor("orange")             
pen = turtle.Turtle()
my_num_sides = 6
my_side_length = 70
my_angle = 360.0 / my_num_sides
for i in range(my_num_sides):
   pen.forward(my_side_length)           
   pen.right(my_angle) 
turtle.done()