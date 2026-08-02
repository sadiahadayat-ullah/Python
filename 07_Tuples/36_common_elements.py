tuple1 = (10,20,30,40,50)
tuple2 = (30,40,60,80)
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
common_elements = ()
for num in tuple1:
    if num in tuple2  and num not in common_elements:
        common_elements = common_elements + (num,)
print("Common elements:", common_elements)
