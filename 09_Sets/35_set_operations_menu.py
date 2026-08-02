set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
while True:
    print("\n=====Set Operations Menu=====")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (set1 - set2)")
    print("4. Symmetric Difference")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting...")
        break
    if choice == 1:
        print("Union:",set1 | set2)
    elif choice == 2:
        print("Intersection:",set1 & set2)
    elif choice == 3:
        print("Difference:",set1 - set2)
    elif choice == 4:
        print("Symmetric Difference:",set1 ^ set2)
    else:
        print("Invalid Choice")
