numbers = {1,2,3,4,6,7}
print("Missing number:")
for i in range(1,8):
    if i not in numbers:
        print(i)
