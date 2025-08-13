# Number Guessing Game
import random

print("Welcome to Number Guessing Game!!")
print("INSTRUCTIONS:")
print("Enter a number which would act as range for the numbers you will guess")
top_result = int(input("Enter a number:"))
guess = 0
if top_result <= 0:
    print("Enter a number greater then zero next time  ")
    quit()

random_number = random.randint(0, top_result)
while True:
    guess += 1
    user_guess = int(input("Make your guess: "))
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("You are below the number!")
        continue
    else:
        print("You are above the number!")
print("You took", guess, "guesses")
