# Program: Number Guessing Validator
# Description: Valid number guess using exception handling

secret = 7

try:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Correct Guess!")
    else:
        raise ValueError("Wrong guess. Try again")
except ValueError as e:
    print(e)

finally:
    print("Program ended")
