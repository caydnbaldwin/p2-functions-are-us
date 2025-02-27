# Generate a random number between 0 and 50
# Get a number from the keyboard between 0 and 50 (tell user)
# Tell the user if the number is too high or too low
# Continue this process until the user guesses the number

import random 

inumber = random.randint(0,50) 
print("Can you guess the number between 0 and 50?")
user= int(input("What is your guess?"))
while user != inumber:
    if user > inumber:
        print("Too high")
    else:
        print("Too low")
    user= int(input("What is your guess?"))
print("You guessed it!")

