def averageGrades(student):
    total = 0
    
    for grade in student:
        total += grade
        # total = total + grade
    
    average = total / len(student)
    
    return average

studentsGrades = [[98.0, 76.5, 83.5, 83.0],
                  [82.7, 77.0, 90.2, 93.0],
                  [83.0, 85.2, 68.0, 91.0],
                  [72.0, 75.6, 92.5, 83.0] ]
                  
for student in studentsGrades:
    averageGrade = round(averageGrades(student), 1)
    print("Average: " + str(averageGrade))
    