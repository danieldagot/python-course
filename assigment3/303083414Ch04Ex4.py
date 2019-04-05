gradesSum = 0
greatestGrade = 0
numGrades = 0

grade = float( input( 'Please enter grade: ' ) )

while grade != 777:
    if grade != 777:
        numGrades = numGrades + 1

        if grade > greatestGrade:
            greatestGrade = grade

        gradesSum += grade

    grade = float( input( 'Please enter grade: ' ) )

gradesAvg = gradesSum / numGrades
print 'The average is ' + str( gradesAvg )

gradesAvg = (gradesSum - greatestGrade) / (numGrades - 1)
print 'The average after removing the greatest grade is: ' + str( gradesAvg )
