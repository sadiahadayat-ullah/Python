tuple1 = (10,20,30,40,50)
tuple2 = (30,40,60,80)
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
unique_elements = ()
for num in tuple1:
    if num not in tuple2 and num not in unique_elements:
        unique_elements += (num,)
for num in tuple2:
    if num not in tuple1 and num not in unique_elements:
        unique_elements += (num,)
print("Unique elements:", unique_elements)