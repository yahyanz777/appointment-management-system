# Problem Set 2, hangman.py
# Name: Mohamed Hussien
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


# -----------------------------------
# Problem 2: Helper Functions
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else:
            guessed_word.append("_ ")
    return "".join(guessed_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available = []
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available.append(char)
    return "".join(available)


# -----------------------------------
# Problem 3: Basic Hangman Game
# -----------------------------------

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()

        # Check for invalid input (non-alphabetic or not length 1)
        if not user_input.isalpha() or len(user_input) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

        # Check if already guessed
        elif user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

        # Valid new guess
        else:
            letters_guessed.append(user_input)
            
            if user_input in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                # Deduct 2 guesses for vowels, 1 for consonants
                if user_input in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

        print("------------")

    # Game over conditions
    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        total_score = guesses_remaining * unique_letters
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# -----------------------------------
# Problem 4: Hangman with Hints
# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all actual letters match and length matches; False otherwise
    '''
    # Strip away all spaces from my_word (represented as '_ ')
    stripped_my_word = my_word.replace(" ", "")

    if len(stripped_my_word) != len(other_word):
        return False

    revealed_letters = set(char for char in stripped_my_word if char != '_')

    for i in range(len(stripped_my_word)):
        char_my = stripped_my_word[i]
        char_other = other_word[i]

        if char_my != '_':
            if char_my != char_other:
                return False
        else:
            # An underscore cannot represent a letter that has already been revealed
            if char_other in revealed_letters:
                return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, prints out every word in wordlist that matches my_word
    '''
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)

    if matches:
        print("Possible word matches are:")
        print(" ".join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman with hint capabilities (*).
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()

        # Special hint mechanism
        if user_input == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        # Check for invalid input (non-alphabetic or not length 1)
        elif not user_input.isalpha() or len(user_input) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

        # Check if already guessed
        elif user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

        # Valid new guess
        else:
            letters_guessed.append(user_input)
            
            if user_input in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                if user_input in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

        print("------------")

    # Game over conditions
    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        total_score = guesses_remaining * unique_letters
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# -----------------------------------
# Driver Code to run the game
# -----------------------------------

if __name__ == "__main__":
    # To run standard Hangman:
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    # To run Hangman with Hints:
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)