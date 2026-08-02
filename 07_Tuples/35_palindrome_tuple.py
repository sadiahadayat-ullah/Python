numbers = (10,20,30,10,20)
print("Tuple:", numbers)
reverse = ()
# Check whether palindrome tuple or not
for num in numbers:
    reverse = (num,) + reverse
if numbers == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")