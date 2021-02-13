
# Imports
import re, sys, random, time
from string import ascii_lowercase



# Importing text file as list
words = open('heart2.txt').read()
damn = re.findall(r'\w+', words)

# Choosing a word with some parameters
def choose():
    for i in range(len(damn)):
        mainWord = random.choice(damn)
        if len(mainWord) < 4:
            continue
        if len(mainWord) > 10:
            continue
        else:
            for i in range(len(mainWord)):
                if mainWord[i] in ascii_lowercase:
                    pass
                else:
                    continue
        break

    return mainWord

# Main loop
fred = False
try:
    while True:
        # Setup
        guesses = 0
        letters = []
        print('Welcome to Hangman!')
        time.sleep(.8)
        print('Guesses taken = ' + str(guesses) + '/7')
        time.sleep(.8)
        chosen = choose()

        # Saying how long the word is
        print('My word is ' + str(len(chosen)) + ' letters long.')
        time.sleep(.8)

        # Convert the word to a last of characters
        man = []
        for i in range(len(chosen)):
            man.append(chosen[i])

        # Create and print a blank board
        glue = (' ' * len(chosen))
        board = []

        for i in range(len(chosen)):
            board.append(glue[i])
        print('The word: ', end='')
        time.sleep(.8)

        for i in range(len(board)):
            if i == (len(board) - 1):
                if board[i] == ' ':
                    print(' _')
                else:
                    print(' ' + board[i])
            elif board[i] == ' ':
                print(' _', end='')
            else:
                print(' ' + board[i], end='')
        Fred = True

        while Fred:

            # Check to see if the word has been guessed
            if ' ' not in board:
                print('Congratulations, you win.')
                print('Do you want to play again? (Type YES or NO and press ENTER)')
                answer = input()
                if answer == 'NO' or answer == 'no':
                    sys.exit()
                elif answer == 'YES' or answer == 'yes':
                    Fred = False
                    continue

            time.sleep(.8)
            # User guesses a letter
            print('Guess a letter or the word.')
            guessed = input()

            # Allows user to guess the whole word
            if guessed in ascii_lowercase:
                pass
            else:
                if guessed == chosen:
                    print('Correct, you win.')
                    print('Do you want to play again? (Type YES or NO and press ENTER)')
                    answer = input()

                    if answer == 'NO' or answer == 'no':
                        sys.exit()
                    elif answer == 'YES' or answer == 'yes':
                        Fred = False
                        continue
                    else:
                        pass
                else:
                    print('Sorry, that is incorrect.')
                    guesses += 1
                    continue

            # Checks if the guessed letter is in the word or not
            if guessed in man:
                for i in range(len(chosen)):
                    if guessed == man[i]:
                        board[i] = man[i]
                    else:
                        pass
                print('Correct.')
            else:
                print('Sorry, that is incorrect.')
                letters.append(guessed)
                guesses += 1
            time.sleep(.8)

            # Checks if the user ran out of guesses
            if guesses >= 7:
                print('Sorry, you ran out of guesses. The man was hanged. The word was "' + chosen + '".')
                print('Do you want to play again? (Type YES or NO and press ENTER)')
                answer = input()
                if answer == 'NO' or answer == 'no':
                    sys.exit()
                elif answer == 'YES' or answer == 'yes':
                    Fred = False
                    continue
                else:
                    pass
            else:
                pass

            # Prints number of wrong guesses
            print('Number of wrong guesses = ' + str(guesses) + '/7. ')
            time.sleep(.8)

            # Prints a list of incorrectly guessed letters
            if len(letters) == 0:
                print('Incorrectly guessed letters: ')
            else:
                print('Incorrectly guessed letters: ', end='')
            for i in range(len(letters)):
                print(' ' + letters[i])

            time.sleep(.8)

            # Prints the board
            print('The word: ', end='')
            time.sleep(.8)

            for i in range(len(board)):
                if i == (len(board) - 1):
                    if board[i] == ' ':
                        print(' _')
                    else:
                        print(' ' + board[i])
                elif board[i] == ' ':
                    print(' _', end='')
                else:
                    print(' ' + board[i], end='')
            time.sleep(.8)
        continue

except KeyboardInterrupt:
    sys.exit()
