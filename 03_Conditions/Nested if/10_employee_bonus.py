years = int(input("Enter the number of years: "))
performance = int(input("Enter the performance: "))
if years >= 10:
    if performance >= 60:
        print("Bonus - $1000")
    elif performance >= 50:
        print("Bonus - $500")
    elif performance >= 25:
        print("Bonus - $25")
    else:
        print("Poor performance")
else:
    print("No bonus")