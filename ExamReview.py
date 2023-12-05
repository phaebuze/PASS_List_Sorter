# Phaedra's PASS Exam Review
# Dec. 05

# Write a Python function that takes a list of integers as input and 
# returns the sum of all the even numbers in the list.

def evenNumbers(numberList):
    sumVal = 0
    
    for num in numberList:
        if (num % 2 == 0):
            sumVal += num
    
    return sumVal

numberList = []

while (len(numberList) < 10):
    number = input("Enter an int: ")
    
    # data validation
    if (number.isdigit()):
        numberList.append(int(number))
        print("added")
    else:
        print("invalid input")


sumOfEven = evenNumbers(numberList)


# Write a program that asks the user to enter a list of integers, 
# one at a time, until they enter the value 0. 
# The program should then compute and print the sum of all the positive integers entered, 
# and the product of all the negative integers entered. 
# Assume user enters a valid integer.

numberList = []

number = int(input("Enter an int: "))

while (number != 0):
    numberList.append(number)
    number = int(input("Enter an int: "))
    
positiveSum = 0
negativeProduct = 1

for num in numberList:
    if(num > 0):
        positiveSum += num
        
    elif(num < 0):
        negativeProduct *= num 
    
print("Positive sum: "  + str(positiveSum))
print("Negative product: ", negativeProduct)


# count lower case letters in list
mylist = ["Hello", "world", "I", "am", "an", "AI", "assistant"]

def count_lowercase_letters(wordList):
    lowercaseCount = 0
    
    for string in wordList:      
        for char in string:
            if (char.islower()):
                lowercaseCount += 1
        
    return lowercaseCount
    
    
lowerCount = count_lowercase_letters(mylist)

print("Lowercase letters in list:", lowerCount)

print(sumOfEven)


# flowchart implementation
F = float(input("Enter a F temp: "))

C = (F+32) * (5/9)

if C > 15:
    print("Good Weather")
else:
    print("Cool Weather")


# create list based on user input
def createList(number):
    numberList = []
    
    for i in range(0, number+1):
        numberList.append(i)
    
    return numberList

number = int(input("Enter an int between 0-20 (exclusive): "))

while (number <= 0 or number >= 20):
    number = int(input("Enter an int between 0-20 (exclusive): "))

numberList = createList(number)

print(numberList)


# data validation
# Code Format: AAA-PPP-CC 

code = input("Enter product code: ")

valid = False

if (len(code) == 10):
    if (code[3] == "-" and code[7] == "-"):
        AAA = code[0:3]
        if (AAA.isdigit()):
            AAA = int(AAA)
            if (AAA >= 111 and AAA <= 999):
                PPP = code[3:6]
                for p in PPP:
                    if (p.isdigit() or p.isalpha()):
                        CC = code[8:]
                        if (CC.isdigit()):
                            CC = int(CC)
                            if (CC >= 00 and CC <= 99):
                                valid = True

if (valid):
    print("Code is valid")
else:
    print("Code is invalid")


# string splicing
string = input("Enter a string: ")
newString = ""

for i in range(0, len(string)):
    if (i == 0 ):
        newString += string[i].upper()
    elif(string[i-1] == " "):
        newString += string[i].upper()
    else:
        newString += string[i]
        
print(newString)
