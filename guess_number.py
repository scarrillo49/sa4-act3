import random

number = random.randint(1, 100)  

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ").lower()  

    if guess == 'q':
        print(f"The number was {number}.")
        break

    try:
        guess = int(guess)  

        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        else:
            print("Try again!")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

print("Thanks for playing!")
