# fruit list example
fruitList = ["Cherry", "Pineapple", "Peach", "Mango", "Grape", "Banana"]
print(fruitList)

# add items to list
fruitList.append("Orange")
fruitList.append("Watermelon")
print(fruitList)

# remove item from lsit
fruitList.remove("Cherry")

# print items
for fruit in fruitList:
    print(fruit)
    
# number list example
numberList = [1,2,3,4,5,6,7,8,9,10]

# using a for loop - first 3 index
for i in range(0, len(numberList)):
    if (i < 3):
        print(numberList[i])
        
# simple way - print first 3 index
print(numberList[0:3])

# last 3 elements
print(numberList[7:])

# elements 3 to 7
print(numberList[3:8])