def gcd(num1,num2):
    GCD = 1
    for i in range(1,min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            GCD = i
    return GCD
print("GCD: ",gcd(12,18))