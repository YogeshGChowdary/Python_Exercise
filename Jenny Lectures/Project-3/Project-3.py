### Hangman Game ###
import random

word_list = ['apple', 'beautiful', 'potato']   # word defined earlier and user has to guess  the word by seeing the empty spaces equal to no. of chars in word
lives = 6
chosen_word = random.choice(word_list)
#print(chosen_word)

# generating empty spaces equal to no. of chars in chosen word
display = []
for i in chosen_word:
    display += '_'
print(display)

game_over = False
while not game_over:
    guessed_letter = input('guess a letter: ').lower()
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:   # here guessed letter is checked against all
                                       # positons in chosen word -> becsuase of for loop
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You Lose')
    if '_' not in display:
        game_over = True
        print('You Win!!')
