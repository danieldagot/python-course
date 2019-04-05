numGrades = int( input( 'Please enter the number of grades: ' ) )
gradesSum = 0
greatestGrade = 0

for x in range( 1, numGrades + 1 ):
    grade = float( input( 'Please enter grade: ' ) )

    if grade > greatestGrade:
        greatestGrade = grade

    gradesSum += grade

gradesAvg = gradesSum / numGrades
print 'The average is ' + str( gradesAvg )

gradesAvg = (gradesSum - greatestGrade) / (numGrades - 1)
print 'The average after removing the greatest grade is: ' + str( gradesAvg )
