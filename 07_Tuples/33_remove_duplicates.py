numbers = (10,20,30,10,35,20)
print("Tuple:", numbers)
unique = ()
# Remove duplicates in the tuple
for num in numbers:
    if num not in unique:
        unique += (num,)
print("Tuple after removing duplicates:", unique)