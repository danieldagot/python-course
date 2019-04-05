import turtle

hours = -1
minutes = -1

while hours < 0 or hours > 23:
    hours = int( input( 'Please enter hours (between 00 to 23): ' ) )

while minutes < 0 or minutes > 59:
    minutes = int( input( 'Please enter minutes (between 0 to 59): ' ) )

pen = turtle.Turtle()

pen.tracer( 0 )
pen.speed( 0 )

for i in range( 12 ):
    pen.pensize(2)
    pen.penup()
    pen.forward( 180 )
    pen.pendown()
    pen.forward( 30 )
    pen.penup()
    pen.forward( 40 )
    pen.backward( 250 )
    pen.left( 360 / 12 )
    pen.pensize(1)

for i in range( 60 ):
    pen.penup()
    pen.forward( 180 )
    pen.pendown()
    pen.forward( 22 )
    pen.penup()
    pen.forward( 48 )
    pen.backward( 250 )
    pen.left( 360 / 60 )

pen.color( 'red' )
pen.penup()
pen.goto( 0, 0 )
pen.setheading( 90 )
pen.right( hours * 360 / 12 )
pen.pendown()
pen.forward( 100 )

pen.color( 'black' )
pen.penup()
pen.goto( 0, 0 )
pen.setheading( 90 )
pen.right( minutes * 360 / 60 )
pen.pendown()
pen.forward( 150 )

pen.getscreen().update()

turtle.mainloop()
