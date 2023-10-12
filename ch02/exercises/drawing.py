import turtle

sides = int(input("enter the number of sides for the shape "))
print(sides)

length = int(input("what is the length of the sides "))
print(length)

internal_angle = 360/sides
print(internal_angle)

shape_turtle = turtle.Turtle()
shape_turtle.color("blue")

for i in range(sides):
    shape_turtle.forward(length)
    shape_turtle.right(internal_angle)


window = turtle.Screen()
window.exitonclick()
