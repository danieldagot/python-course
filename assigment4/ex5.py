import turtle

hours = -1
minutes = -1

while hours < 0 or hours > 23:
    hours = int( input( 'Please enter hours (between 00 to 23): ' ) )

while minutes < 0 or minutes > 59:
    minutes = int( input( 'Please enter minutes (between 0 to 59): ' ) )

pen = turtle.Turtle()

pen.shape( 'arrow' )
pen.tracer( 0 )
pen.speed( 0 )
pen.penup()
pen.goto( 0, -180 )
pen.pendown()
pen.color( 'black' )
pen.circle( 180 )

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
