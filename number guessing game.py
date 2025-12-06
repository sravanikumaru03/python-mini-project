import random

print("🎯 Welcome to Number Guessing Game! 🎯")
number = random.randint(1, 20)   # computer selects number
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {number}.")
        print(f"You guessed it in {attempts} attempts!")
        break
