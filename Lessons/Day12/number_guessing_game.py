import random

def start_game():
    
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose dificulty level. Type 'easy' or 'hard': ")

    lives = 0
    
    final_number = random.choice(range(1,101))
    if difficulty_level == 'easy':
        lives = 10
    elif difficulty_level == 'hard':
        lives = 5
    else:
        print("Unsupported difficulty level. Try again!")
        start_game()

    while lives >= 0:
        
        if lives == 0:
            print("You've run out of guesses, you lose.")
            break

        print(f'You have {lives} attempts remaining to guess the number.')
        guess = int(input("Make a guess: "))
        
        if final_number == guess:
            print(f'You got it! The answer was {final_number}.')
            break
        elif final_number > guess:
            print('Too low.')
            lives -= 1
        elif final_number < guess:
            print('Too high.')
            lives -= 1

start_game()