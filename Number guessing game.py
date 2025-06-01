#Number Guessing Game
from random import randint
random_number = randint(1,100)
num = int(input("Enter a number between 1 and 100: "))
if num < random_number:
     print("Your guess is too low")
elif num > random_number:
     print("Your guess is too high")
else:
      print("Your guess is correct!")
print("Thank you for playing")
print("Random number was:", random_number)
# This code generates a random number between 1 and 100 and asks the user to guess it.
