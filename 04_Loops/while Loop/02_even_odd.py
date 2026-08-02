n = 1
odd_count = 0
while n <= 20:
    if n%2 == 0:
        print("Even:",n)
    else:
        odd_count += 1
    n += 1
print("Total odd numbers from 1 to 20:", odd_count)