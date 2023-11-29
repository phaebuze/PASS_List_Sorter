# Phaedra's PASS Test 3 Review

# --- LOOP EXERCISES --- #
# star patterm
user_input = input('ENTER the number: ')

for i in range(1, int(user_input)+1):
    print(i * '*')


# GCD
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

count = 1

while (count <= min(num1, num2)):
    if (num1 % count == 0 and num2 % count == 0):
        GCD = count
    count += 1
    
print("GCD: ", GCD)


# number of vowels
    # method 1
vowelList = ['a', 'e', 'i', 'o', 'u', 'y']
vowelCount = 0

for char in myString:
    for vowel in vowelList:
        if (char == vowel):
            vowelCount += 1
    
print("Number of vowels: ", vowelCount)

    # method 2
vowelCount = 0

for i in myString:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y'):
        vowelCount += 1
    
print("Number of vowels: ", vowelCount)


# reverse a string
myString = input("Enter a string: ")

    # method 1
print(myString[::-1])

    # method 2
for i in reversed(myString):
    print(i)

    # method 3
for i in range(len(myString)-1, -1, -1):
    print(myString[i])


# --- LIST EXERCISES --- #
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List slicing
# first 5 index
print(myList[:5])

for i in range(0, 5):
    print(myList[i])
    
count = 0
while (count < 5):
    print(myList[count])
    count += 1

# even index
print(myList[0::2])

for i in range(0, len(myList)):
    if (i % 2 == 0):
        print(myList[i])

# list manipulation
# add element
myList.append(11)
print(myList)

# insert element
myList.insert(3, 3.5)
print(myList)

# remove elelemt
myList.remove(3.5)
print(myList)

# remove index
myList.remove(myList[-1])
    # myList.remove(myList[10])
print(myList)

# list searching
fruits = ["apple", "orange", "pear", "grape", "apple", "watermelon", "apple", "orange", "strawberry"]

# element present
element1 = "watermelon"
element2 = "kiwi"

if element1 in fruits:
    print(element1, "is in list!")
else:
    print(element1, "is not in list!")
    
if element2 in fruits:
    print(element2, "is in list!")
else:
    print(element2, "is not in list!")

# find the index
fruitSearch = "grape"
for i in range(0, len(fruits)):
    if (fruits[i] == fruitSearch):
        print("Index of search: ", i)
        break

# 2D list
calendar = [["January", 31],
            ["February", 28.25],
            ["March", 31],
            ["April", 30],
            ["May", 31],
            ["June", 30],
            ["July", 31],
            ["August", 31],
            ["September", 30],
            ["October", 31],
            ["November", 30]]

# add December to list
calendar.append(["December", 31])

# print specific item
birthMonth = "November"

for months in calendar:
    if months[0] == birthMonth:
        print("Number of days in ", birthMonth, ": ", months[1])

