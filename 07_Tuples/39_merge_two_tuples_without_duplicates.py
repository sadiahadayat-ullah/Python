tuple1 = (10,20,30,40,50)
tuple2 = (50,60,30,20)
# Merge two tuples
result = tuple1 + tuple2
print("Merged Tuple:",result)
unique_elements = ()
# Remove duplicates elements
for num in result:
    if num not in unique_elements:
        unique_elements += (num,)
print("Unique Elements:",unique_elements)