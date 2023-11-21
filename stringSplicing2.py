# string exercises

myString = "Python Programming is Fun"

# print ever second character (every other)
for i in range(0, len(myString)):
    if (i%2 != 0):
        print(myString[i])
        
# last 3 letters
print(myString[-3:])

# number of 'O'
for char in myString:
    if (char == "o"):
        print(myString[char])