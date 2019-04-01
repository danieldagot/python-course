import turtle

# Set all the different colors anf dimensions
turtle.title('303083414As02')
turtle.hideturtle()
turtle.setup(width=510, height=430)
turtle.speed(5)
turtle.begin_fill()
turtle.pensize(3)
turtle.pencolor('yellow')
turtle.fillcolor('pink')

# Draw the triangle
turtle.forward(175)
turtle.left(120)
turtle.forward(175)
turtle.left(120)
turtle.forward(175)
turtle.left(120)

turtle.end_fill()

turtle.bgcolor('green')

# Set text
turtle.pencolor('black')
turtle.penup()
turtle.goto(-85, 180)
turtle.pendown()
turtle.write('Omer Morad - 303083414', align='center', font=('Arial', 20, 'bold'))

turtle.mainloop()
