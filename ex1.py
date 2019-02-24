import turtle

turtle.title('303083414As02')
turtle.hideturtle()
turtle.speed(5)
turtle.begin_fill()
turtle.pensize(3)
turtle.pencolor('yellow')
turtle.fillcolor('pink')
turtle.setup(width=510, height=430)

turtle.forward(175)
turtle.left(120)
turtle.forward(175)
turtle.left(120)
turtle.forward(175)
turtle.left(120)

turtle.end_fill()

turtle.bgcolor('green')
turtle.pencolor('black')

turtle.write('Omer Morad - 303083414', align='center', font=('Arial', 20, 'bold'))

turtle.mainloop()
