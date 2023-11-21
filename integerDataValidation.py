# ask for input
userInput = input("Enter an integer: ")

# while input is not integer
while (not userInput.isdigit()):
    userInput = input("Enter an integer: ")
    
print(userInput + " is an integer")