lapDistance = 400
distance = int( input( 'Please enter distance to run:' ) )
distanceLeft = int( distance )

for run in range( 0, distance, 400 ):
    if distanceLeft <= 400:
        print('This is the last lap')
    else:
        print('You have more distance left: ' + str( distanceLeft ))
    distanceLeft -= 400
