string = "Hello, world!"
stringLength = 12

# print just the words
print(string[0:5] + " " + string[7:12])

# print string backwords
for i in range(stringLength, -1, -1):
  print(string[i])

# convert to uppercase
print(string.upper())

# starts with 'Hello'
startsWith = "Hello"

string = string.lower()

emptyString = ""

for char in string:
    print("Char: ", char)
    emptyString += char
    print(emptyString)
    
    if (emptyString == startsWith):
        print("matched")
        break

# simpler version
if (startsWith in string):
    print("yes") 

