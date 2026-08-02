num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
for i in range(max(num1, num2),(num1*num2)+1):
    if i % num1 == 0 and i % num2 == 0:
        print("LCM:",i)
        break