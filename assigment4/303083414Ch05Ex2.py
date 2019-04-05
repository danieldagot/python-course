import turtle


def triangle( pen, forward ):
    for k in range( 0, 3 ):
        pen.forward( forward )
        pen.left( 120 )


def draw_snail( pen, n, left, forward, k ):
    for j in range( 0, n ):
        triangle( pen, forward )
        pen.left( left )
        forward = k * forward


def main( pen ):
    pen.speed( 0 )
    draw_snail( pen, 31, 10, 200, 0.97 )
    turtle.mainloop()


t = turtle.Turtle()
main( t )
