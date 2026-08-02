a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter operation(+,-,*,/,//,%,**):")
if op == "+":
    print("Result",a+b)
elif op == "-":
    print("Result",a-b)
elif op == "*":
    print("Result",a*b)
elif op == "/":
    print("Result",a/b)
elif op == "//":
    print("Result",a//b)
elif op == "%":
    print("Result",a%b)
elif op == "**":
    print("Result",a**b)
else:
    print("Invalid operation")