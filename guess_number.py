import random

number = random.randint(1, 100)  
MAX_GUESSES = 5
print("I'm thinking of a number...")

for guesses in range(1, MAX_GUESSES + 1):
    guess = int(input(f"Guess {guesses}/{MAX_GUESSES}: "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")

    try:
        guess = int(guess)  

        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

print("Thanks for playing!")
