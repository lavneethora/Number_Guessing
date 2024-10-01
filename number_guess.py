import random
from art import number_guessing_logo
    
number = random.randint(1,101)

print(number_guessing_logo)
print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

def play_game():
    global difficulty
    if difficulty == 'easy':
        print("You have 10 attempts to guess the number.")
        guess_counter = 10
        for i in range(10):
            guess = int(input("Make a guess: "))
            if guess == number:
                print("You have guessed the number!")
                break
            else:
                guess_counter -= 1
                print(f"Incorrect guess. {guess_counter} attempts remaining.")
                if guess > number:
                    print("Your number is high. Guess low.")
                elif guess < number:
                    print("Your number is low. Guess higher.")
    elif difficulty == 'hard':
        print("You have 5 attempts to guess the number.")
        guess_counter = 5
        for i in range(5):
            guess = int(input("Make a guess: "))
            if guess == number:
                print("You have guessed the number!")
                break
            else:
                guess_counter -= 1
                print(f"Incorrect guess. {guess_counter} attempts remaining.")
                if guess > number:
                    print("Your number is high. Guess low.")
                elif guess < number:
                    print("Your number is low. Guess higher.")
    else:
        print("Wrong Input.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        play_game()
        
play_game()