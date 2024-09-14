import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1 Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word. At that point display has no more blanks ("_"). Then you can tell the user they have won.
game_over = False
correct_letter = []
while not game_over:
    guess = input("Guess the letter: ").lower()
    display = ""
    # TODO-2 Change the for loop so that you keep the previous correct.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("You Win")
