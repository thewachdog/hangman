import random
import hangmanascii

selectedword = random.choice(hangmanascii.wordlist)
selectedword_list = list(selectedword)

hangmanascii.title()


lives = 6
for letter in range(0, len(selectedword_list)):
        selectedword_list[letter] = '_'

# game starts here
while selectedword_list.count('_') > 0:
        guess = input('\nGuess a letter : ').lower()

        # if user already guessed it
        if guess in selectedword_list:
                print("\n You already guessed it.")

        # prints hangman
#       print(f'\n{hangmanascii.hangman[lives]}\n')

        # checking the guess is right
        for letter in range(0, len(selectedword)):
                if guess == selectedword[letter]:
                        selectedword_list[letter] = selectedword[letter]

                        # prints hangman
                        print(f'\n{hangmanascii.hangman[lives]}\n')

        print('\n')
        #print the letters
        for letter in selectedword_list:
                print(letter, end = ' ')

        # prints hangman
#       print(f'\n{hangmanascii.hangman[lives]}\n')

        # if user have won
        if selectedword_list.count('_') == 0:
                print('\nYou won !!\n')

        # if user guessed wrong
        if guess not in selectedword_list:
                lives -= 1
                # prints hangman
                print(f'\n{hangmanascii.hangman[lives]}\n')

                print(f'Oops!! Your guess is wrong. Now you have {lives} lives left\n')

                #if user have lost
                if lives == 0:
                        print('\nGame over :(')
                        break
