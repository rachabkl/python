import turtle

# Create the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # background color

# Create the turtle
t = turtle.Turtle()
t.color("red")                # turtle (pen) color
t.pensize(4)                  # line thickness
t.speed(3)                    # drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Move the turtle a bit
t.penup()
t.goto(-50, 50)
t.pendown()

# Draw the square
draw_square(100)

# End the program when clicked
screen.exitonclick()
