cost = 400
startWeight = float( input( 'Enter your weight in the beginning of the month: ' ) )
endWeight = float( input( 'Enter your weight in the end of the month: ' ) )

difference = int( startWeight - endWeight )

if difference > 0:
    percentage = difference / startWeight * 100
    discount = int( percentage * 10 )
    toPay = cost - discount

    print '''
        You saved ''' + str( discount ) + ''' Shekels
        Lost around ''' + str( difference ) + '''kg
        Your monthly payment is ''' + str( toPay ) + ''' Shekels'''
else:
    print 'You don\'t deserve any discount, keep working!'
