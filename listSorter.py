# Phaedra's PASS Session
# List sorting program

# empty list of numbers
studentGrades = [["John", 95], ["Phaedra", 89]]


def maxVal():
    maximum = studentGrades[0][1]
    
    for student in studentGrades:
        if student[1] > maximum:
            maximum = student[1]
      
    return maximum


def minVal():
    minimum = studentGrades[0][1]

    for student in studentGrades:
        if student[1] < minimum:
            minimum = student[1]

    return minimum


def sumVal():
    sumVal = 0
    
    for student in studentGrades:
        sumVal += student[1]
        
    return sumVal  

def avgVal():
    
    average = sumVal() / len(studentGrades)
    
    return average


def addToList():
    quitString = "not yet"

    while (quitString != "Q"):
        name = input("Enter your name: ")
        grade = input("Enter your GPA, or 'Q' to stop: ")

        if (grade == "Q"):
            quitString = grade
        elif (grade.isdecimal()):
            studentGrades.append([name, grade])


while(True):
    print("Choices: \n1. Maximum \n2. Minimum \n3. Sum \n4. Average \n5. Add numbers \n6. Show all numbers in list\n7. Exit")
    choice = int(input("Enter a choice: "))
    if (choice == 1):
        # max of list
        maximumValue = maxVal()
        print("Max value of the list: ", maximumValue)
        
    elif(choice == 2):
        # min of list
        minimumValue = minVal()
        print("Min value of the list: ", minimumValue)
        
    elif(choice == 3):
        # sum of list
        sumResult = sumVal()
        print("Sum of list values: " + str(sumResult))
        
    elif(choice == 4):
        # average of list
        average = round(avgVal(), 2)
        print("Average of list values: " + str(average))
        
    elif(choice == 5):
        # adding numbers to list
        addToList()
        print("Number added to list")
        
    elif(choice == 6):
        # show all grades
        for student in studentGrades:
            print("Name: ", student[0], " - GPA: ", student[1], "%")

    elif(choice == 7):
        # exit the program
        break
    
        



