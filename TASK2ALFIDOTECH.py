import random

def guess_the_number():
    """
    Plays a number guessing game where the user tries to guess a randomly
    generated number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guess_the_number()
