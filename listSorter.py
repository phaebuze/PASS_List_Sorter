# Phaedra's PASS Session
# List sorting program

# List of numbers
numbers = [1, 3, 4, 17, 25, 32, 71, 90]


def maxVal():
    pass

def minVal():
    pass

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
        maxVal()
        
    elif(choice == 2):
        minVal()
        
    elif(choice == 3):
        # sum of list
        sumResult = sumVal()
        print("Sum of list values: " + str(sumResult))
        
    elif(choice == 4):
        # average of list
        average = avgVal()
        print("Average of list values: " + str(average))
        
    elif(choice == 5):
        break
    
        



