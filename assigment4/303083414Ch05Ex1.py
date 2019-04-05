# Calculates if there is an extra payment for kids
def calculate_kids_payment( kids ):
    return kids * 150


# Calculates there is a need to complete the income
def complete_income( income ):
    if income < 5000:
        return 5000 - income

    return 0


# Main program
def main( ):
    income = float( input( 'Please enter your income: ' ) )
    under_eighteen_kids = int( input( 'Please enter the number of kids under the age of 18: ' ) )
    income_completion = complete_income( income )
    extras_for_kids = calculate_kids_payment( under_eighteen_kids )
    print('Total extra for salary is ' + str( extras_for_kids + income_completion ))


main()
