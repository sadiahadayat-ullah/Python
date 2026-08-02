list1 = [10,20,30,40,50]
list2 = [20,35,45,50,30]
print("List1:",list1)
print("List2:",list2)
common_elements = []
for num in list1:
    if num in list2:
        common_elements.append(num)
print("Common Elements:", common_elements)