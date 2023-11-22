import random

word_list = ["ardvark", "baboon", "camel"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

blanks_list = []
for i in range(0, len(chosen_word)):
    blanks_list.append("_")

while "_" in blanks_list:
    
    guess = input("Guess a letter: ").lower()

    counter = 0

    correct_guess = False

    for letter in chosen_word:
        

        if letter == guess:
            blanks_list[counter] = guess
            correct_guess = True
        
        counter += 1

    print(''.join(blanks_list))
    
    if not correct_guess:
        lives -= 1
        print(f'Wrong! Lives remaining = {lives}')

    if lives == 0:
        print("You lost!")
        break
    
if lives > 0:
    print("You won!")