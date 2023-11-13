# Phaedra's PASS Session
# List sorting program

# List of numbers
numbers = [3, 4, 115, 25, 17, 32, 90, 71, 1]


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

flag = False
while(not flag):
    print("Choices: \n1. Maximum \n2. Minimum \n3. Sum \n4. Average \n5. Exit")
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
        # exit the program
        break
    
        



