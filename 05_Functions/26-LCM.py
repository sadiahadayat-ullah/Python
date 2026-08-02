def lcm(num1,num2):
    for i in range(max(num1, num2),num1 * num2 +  1):
        if i % num1 == 0 and i % num2 == 0:
            return i
print("LCM: ",lcm(12,18))