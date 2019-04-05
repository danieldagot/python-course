import turtle


def is_even( number ):
    return number % 2 == 0


def triangle( pen, forward, fill ):
    pen.fillcolor( fill )
    pen.begin_fill()

    for k in range( 0, 3 ):
        pen.forward( forward )
        pen.left( 120 )

    pen.end_fill()


def draw_snail( pen, n, left, forward, k ):
    for j in range( 0, n ):
        if is_even( j ):
            fill = "white"
        else:
            fill = "gray"

        triangle( pen, forward, fill )
        pen.left( left )
        forward = k * forward


def main( pen ):
    pen.speed( 0 )
    draw_snail( pen, 31, 10, 200, 0.97 )
    turtle.mainloop()


t = turtle.Turtle()
main( t )
