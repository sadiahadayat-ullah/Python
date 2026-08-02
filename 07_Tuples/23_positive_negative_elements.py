numbers = (1,2,-3,-4,9,-8,7)
print(numbers)
positive = ()
negative = ()
# Separate positive and negative numbers
for number in numbers:
    if number > 0:
        positive = positive + (number,)
    else:
        negative = negative + (number,)
print("Positive numbers:",positive)
print("Negative numbers:",negative)
# Count positive and negative numbers
print("Length of positive numbers:",len(positive))
print("Length of negative numbers:",len(negative))
