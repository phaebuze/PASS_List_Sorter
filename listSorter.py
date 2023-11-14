# Phaedra's PASS Session
# List sorting program

# empty list of numbers
numbers = []


def maxVal():
    maximum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
      
    return maximum


def minVal():
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


def sumVal():
    sumVal = 0
    
    for num in numbers:
        sumVal += num

    # for i in range(0, len(numbers)):
    #     sumVal += numbers[i]
        
    return sumVal  

def avgVal():
    
    average = sumVal() / len(numbers)
    
    return average


def addToList():
    quitString = "not yet"

    while (quitString != "Q"):
        number = input("Enter a number, or 'Q' to stop: ")

        if (number == "Q"):
            quitString = number
        elif (number.isdecimal()):
            numbers.append(int(number))


flag = False
while(not flag):
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
        # show all numbers
        for grade in numbers:
            print("Grade: ", grade, "%")

    elif(choice == 7):
        # exit the program
        break
    
        



