def length(num):
    count = 0
    for i in num:
        count = count + 1
    return count
number = str(input("Enter a number: "))
length_string = length(number)
print(length_string)