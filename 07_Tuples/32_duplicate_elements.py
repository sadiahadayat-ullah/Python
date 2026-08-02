numbers = (10,20,30,10,35,20)
print("Tuple:", numbers)
seen = ()
duplicates = ()
# Find duplicates in the tuple
for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates += (num,)
    else:
        seen += (num,)
print("Duplicates:", duplicates)
