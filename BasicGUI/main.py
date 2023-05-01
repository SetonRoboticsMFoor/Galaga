import random

user_guess = 0
game_number = random.randint(1,10)
tries = 0

while user_guess != game_number:
    user_guess = int(input("Enter a number: "))
    if user_guess > game_number:
        print("Too High")
        tries += 1
    elif user_guess < game_number:
        print("Too Low")
        tries += 1

print("You win!!! It took you " , tries , " tries")
