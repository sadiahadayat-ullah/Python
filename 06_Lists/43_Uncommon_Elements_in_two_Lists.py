list1 = [10,20,30,40,50]
list2 = [20,35,45,50,30]
print("List1:",list1)
print("List2:",list2)
uncommon_elements = []
for num in list1:
    if num not in list2:
        uncommon_elements.append(num)
for num in list2:
    if num not in list1:
        uncommon_elements.append(num)
print("Uncommon elements:",uncommon_elements)