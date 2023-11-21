# string exercises
# given string
myString = "Python Programming is Fun"

# print ever second character (every other)
for i in range(0, len(myString)):
    if (i%2 != 0):
        print(myString[i])
        
# last 3 letters
print(myString[-3:])

# number of 'o'
oCount = 0
for char in myString:
    if (char == "o"):
        oCount += 1

print("Number of 'o' in string: " + str(oCount))
        
# number of words
spaceCount = 0
for char in myString:
    if (char == " "):
        spaceCount += 1

wordCount = spaceCount + 1
print("Number of words in string: " + str(wordCount))

# number of vowels
vowelList = ["a", "e", "i", "o", "u", "y"]
vowelCount = 0

for char in myString:
    if (char.lower() in vowelList):
        vowelCount += 1

print("Number of vowels in string: " + str(vowelCount))

# number of upper case
upperCount = 0

for char in myString:
    if (char.isupper()):
        upperCount += 1

print("Number of upper case in string: " + str(upperCount))

# middle character
stringLength = len(myString)
middleIndex = stringLength // 2

if (stringLength % 2 == 0):
    print(myString[middleIndex] + myString[middleIndex + 1])
else:
    print(myString[middleIndex])
