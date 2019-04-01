economical = 6
consumption = int( input( 'Please enter your fuel consumption: ' ) )

if consumption > economical:
    print 'You\'re driving in an un economic mode. If you continue to do so, the benefit will be canceled.'
    consumption = int( input( 'Please enter your fuel consumption: ' ) )

    while consumption > economical:
        print 'Please keep slowing down the car'
        consumption = int( input( 'Please enter your fuel consumption again:' ) )

    print 'Now you are driving economic! Keep on!'
else:
    print 'You are driving economic! Keep on!'
