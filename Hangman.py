import random
import logo_for_hangman
import word_list

stages = logo_for_hangman.stages
game = False
lives = 6
chosen_word = random.choice(word_list.word_list)

print(f"Test:{chosen_word}")

display = []

for i in chosen_word:
    display.append("_")

print(f"{' '.join(display)}")

while not game:

    guess = input("Guess a letter: ").lower()

    for j, v in enumerate(chosen_word):
        if v == guess:
            display[j] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"Letter '{guess}' is not in this word. Try again.\nYou have {lives} more lives")
        if lives == 0:
            game = True
            print("You lost")

    if "_" not in display:
        game = True
        print("You win")
    print(stages[lives])