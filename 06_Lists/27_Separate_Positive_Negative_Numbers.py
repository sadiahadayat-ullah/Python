numbers = [1,2,0,-4,8,-5,0,-6,5]
print("Original list:",numbers)
positive = []
negative = []
zero = []
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)
print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero)
print("Length of Positive numbers:",len(positive))
print("Length of Negative numbers:",len(negative))
print("Length of Zero:",len(zero))
