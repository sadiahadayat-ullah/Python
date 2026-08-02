numbers =(10,20,30,40,50)
print(numbers)
search = int(input("Enter a number: "))
found = False
# Search for an element
for number in numbers:
    if number == search:
        found = True
        break
if found:
    print(search,"is present in the list")
else:
    print(search,"is not present in the list")