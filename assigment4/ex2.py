import turtle


def draw_rectangle( backward ):
    for x in range( 3 ):
        turtle.left( -120 )
        turtle.backward( backward )


def draw_snail( ):
    for i in range( 30, -1, -1 ):
        draw_rectangle( i * 3 + 20 )
        turtle.left( i )


def main( ):
    # Create Window
    turtle.colormode( 255 )

    # Set turtle speed
    turtle.speed( 0 )

    draw_snail()

    turtle.exitonclick()


main()
