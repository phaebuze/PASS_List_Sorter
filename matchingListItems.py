list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

matchList = []

for num1 in list1:
    for num2 in list2:
        if (num1 == num2):
            matchList.append(num1)
            

for number in matchList:
    print("Match", number)
    


# different solution
def common_elements(list1,list2):
    return [element for element in list1 if element in list2]
      
      
print("The common numbers between the lists are: " + str(common_elements(list1,list2)))
