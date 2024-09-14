import random

stages = [
    """
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
]
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep of the track of the number of lives left
#  Set 'lives' to equal 6.
lives = 6

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

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    # TODO-2 If guess is not a letter in the chosen_word, then reduce 'lives' by 1
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loose.")
    if "_" not in display:
        game_over = True
        print("You Win")

    # TODO-3: - Print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
