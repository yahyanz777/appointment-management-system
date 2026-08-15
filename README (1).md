# Assignment: Hangman

This assignment introduces you to creating functions in Python, as well as looping mechanisms for repeating a computational process until a condition is reached.

## Getting Started

Download the files `hangman.py` and `words.txt`, and **save them both in the same directory**. Run `hangman.py` before writing any code to make sure your files are set up correctly. The provided code loads words from a file, and you should see the following output in your shell:

```
Loading word list from file...
55900 words loaded.
```

If you see this output, continue to the game requirements below. If you don't, double-check that both files are saved in the same place.

---

## Problem 1: Basic Hangman

You will implement a variation of the classic word game Hangman. If you're unfamiliar with the rules, see [Hangman on Wikipedia](http://en.wikipedia.org/wiki/Hangman_(game)). This problem is scaffolded — you'll build helper functions first before implementing the full game.

**General behavior to implement:**
1. The computer selects a word at random from the list of available words provided in `words.txt`. Note that `words.txt` contains words in all lowercase letters.
2. The user is given a certain number of guesses at the start.
3. The game is interactive: the user inputs a guess, and the computer either:
   - reveals the letter if it exists in the secret word, or
   - penalizes the user and updates the number of guesses remaining.
4. The game ends when the user guesses the secret word, or runs out of guesses.

---

## Problem 2: Hangman Part 1 — Three Helper Functions

Before writing the full game, implement three helper functions. `hangman.py` includes some already-implemented functions you can use — read their docstrings to understand how to use them.

### 1A) Determine whether the word has been guessed

Implement `is_word_guessed(secret_word, letters_guessed)`:
- `secret_word`: a string
- `letters_guessed`: a list of guessed letters (strings)

Returns `True` if every letter of `secret_word` is in `letters_guessed`, `False` otherwise. You may assume all letters in both inputs are lowercase.

**Example usage:**
```python
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(is_word_guessed(secret_word, letters_guessed))
False
```

### 1B) Getting the user's guess

Implement `get_guessed_word(secret_word, letters_guessed)`:

Returns a string comprised of letters and underscores, based on which letters in `letters_guessed` appear in `secret_word`. Use an underscore followed by a space (`_ `) to represent unknown letters — the space matters, since it makes it clear how many letters are missing.

**Hint:** Think about what information you need to return, where to store it as you loop, and how to build up the result.

**Example usage:**
```python
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(get_guessed_word(secret_word, letters_guessed))
'_ pp_ e'
```

### 1C) Getting all available letters

Implement `get_available_letters(letters_guessed)`:

Returns a string of all lowercase English letters *not* in `letters_guessed`, in alphabetical order. You may assume all letters in `letters_guessed` are lowercase.

**Hint:** `string.ascii_lowercase` gives you all lowercase letters:
```python
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
```

**Example usage:**
```python
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(get_available_letters(letters_guessed))
abcdfghjlmnoqtuvwxyz
```

---

## Problem 3: Hangman Part 2 — The Game

Implement `hangman(secret_word)`, which starts an interactive game between the user and the computer. Use the three helper functions from Problem 2.

Initially, manually set `secret_word` for easier testing. Later, the computer will select the word at random.

### A. Game Architecture

1. The computer selects a random word from `words.txt` (loading/selection functions are already provided).
2. Users start with **6 guesses**.
3. At the start, tell the user how many letters the word contains and how many guesses they have.
4. Before each turn, show the user the remaining (not-yet-guessed) letters.

**Example:**
```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
```

### B. User–Computer Interaction

1. Before each guess, display:
   - guesses remaining
   - all letters not yet guessed
2. Ask the user for one guess at a time.
3. After each guess, tell the user whether the letter is in the word.
4. After each guess, display the word with guessed letters revealed and unguessed letters as underscores.
5. Print dashes (`-----`) after each guess to separate turns.

**Example:**
```
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ a_ _
```

### C. User Input Requirements

1. The user guesses one character at a time, but may type any number, symbol, or letter. Accept both uppercase and lowercase letters as valid guesses.
2. If the user enters anything besides a letter, tell them only letters are valid. The user starts with **3 warnings**:
   - Each invalid input or repeated letter costs one warning.
   - Once warnings run out, invalid input or repeats cost one guess instead.

**Hints:**
- Use `input()` to collect the guess.
- `str.isalpha()` and `str.lower()` are useful here.
- Since `words.txt` is all lowercase, convert user input to lowercase throughout.

### D. Game Rules

1. The user starts with 3 warnings.
2. Non-letter input:
   - If warnings remain → lose one warning, and tell the user how many remain.
   - If no warnings remain → lose one guess instead.
3. Repeated letter (already guessed):
   - If warnings remain → lose one warning, and tell the user how many remain.
   - If no warnings remain → lose one guess instead.
4. Correct, new letter → lose no guesses.
5. **Consonants:** an incorrect, new consonant costs **one** guess.
6. **Vowels:** an incorrect, new vowel costs **two** guesses. Vowels are `a`, `e`, `i`, `o`, `u` — `y` does not count as a vowel.

**Example:**
```
You have 5 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: t
Good guess: ta_ t
------------
You have 5 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: e
Oops! That letter is not in my word: ta_ t
------------
You have 3 guesses left.
Available letters: bcdfghijklmnopqrtuvwxyz
Please guess a letter: e
Oops! You've already guessed that letter. You now have 2 warnings:
ta_ t
```

### E. Game Termination

1. The game ends when the user completes the word or runs out of guesses.
2. If the user runs out of guesses, tell them they lost and reveal the secret word.
3. If the user wins, print a congratulatory message with their score.
4. **Scoring:** `total score = guesses_remaining * number of unique letters in secret_word`

**Example (win):**
```
You have 3 guesses left.
Available letters: bcdfghijklnopquvwxyz
Please guess a letter: c
Good guess: tact
------------
Congratulations, you won!
Your total score for this game is: 9
```

### F. General Hints

- Consider writing additional helper functions as needed.
- Track four pieces of state:
  - `secret_word` — the word to guess
  - `letters_guessed` — letters guessed so far
  - `guesses_remaining` — guesses left (note: vowel and consonant penalties differ)
  - `warnings_remaining` — warnings left (only lost for invalid input or repeat guesses)

### G. Example Game — Winning

```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
You have 3 warnings left.
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! You've already guessed that letter. You have 2 warnings left:
_ a_ _
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: s
Oops! That letter is not in my word.
Please guess a letter: _ a_ _
------------
You have 5 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: $
Oops! That is not a valid letter. You have 1 warnings left: _ a_ _
------------
You have 5 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: t
Good guess: ta_ t
------------
You have 5 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: e
Oops! That letter is not in my word: ta_ t
------------
You have 3 guesses left.
Available letters: bcdfghijklmnopqrtuvwxyz
Please guess a letter: e
Oops! You've already guessed that letter. You have 0 warnings left:
ta_ t
------------
You have 3 guesses left.
Available letters: bcdfghijklmnopqrtuvwxyz
Please guess a letter: e
Oops! You've already guessed that letter. You have no warnings left
so you lose one guess: ta_ t
------------
You have 2 guesses left.
Available letters: bcdfghijklnopquvwxyz
Please guess a letter: c
Good guess: tact
------------
Congratulations, you won!
Your total score for this game is: 6
```

### Example Game — Losing

```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long
You have 3 warnings left.
-----------
You have 6 guesses left
Available Letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _
-----------
You have 4 guesses left
Available Letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ _ _ _
-----------
You have 3 guesses left
Available Letters: cdefghijklmnopqrstuvwxyz
Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _
-----------
You have 2 guesses left
Available Letters: defghijklmnopqrstuvwxyz
Please guess a letter: 2
Oops! That is not a valid letter. You have 2 warnings left: _ _ _ _
-----------
You have 2 guesses left
Available Letters: defghijklmnopqrstuvwxyz
Please guess a letter: d
Oops! That letter is not in my word: _ _ _ _
-----------
You have 1 guesses left
Available Letters: efghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: e_ _ e
-----------
You have 1 guesses left
Available Letters: fghijklmnopqrstuvwxyz
Please guess a letter: f
Oops! That letter is not in my word: e_ _ e
-----------
Sorry, you ran out of guesses. The word was else.
```

Once your code is complete and tested (with a manually-set secret word), scroll to the bottom of the file and find the two commented lines under `if __name__ == "__main__":`

```python
#secret_word = choose_word(wordlist)
#hangman(secret_word)
```

Uncomment these lines and reload your code to play against the computer, which will pick a word at random from the full word list.

---

## Problem 4: Hangman Part 3 — The Game with Hints

Playing Hangman against the computer isn't always easy, especially with an obscure word. This variation, `hangman_with_hints`, lets the player request a hint: guessing the special character `*` prints all words from the loaded list that match the current guessed pattern.

For example, if the hidden word is `tact` and you've guessed `t`, so the pattern is `t_ _ t`, the matching words (from the loaded list) would be:

```
tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit
```

Guessing `*` should **not** cost the user a guess.

To implement this, first complete two helper functions:

### 3A) Matching the current guessed word

Implement `match_with_gaps(my_word, other_word)`:
- `my_word`: an instance of a guessed word, possibly containing `_`'s (e.g. `'t_ _ t'`)
- `other_word`: a normal English word

Returns `True` if the guessed letters in `my_word` match the corresponding letters in `other_word`. Returns `False` if the words differ in length, or if a guessed letter in `my_word` doesn't match the corresponding character in `other_word`.

Note: since guessing a letter reveals *all* its positions in the secret word, an underscore (`_`) can never correspond to a letter that's already been revealed elsewhere in `my_word`.

**Hint:** `strip()` may help when comparing word lengths.

**Example usage:**
```python
>>> match_with_gaps("te_ t", "tact")
False
>>> match_with_gaps("a_ _ le", "banana")
False
>>> match_with_gaps("a_ _ le", "apple")
True
>>> match_with_gaps("a_ ple", "apple")
False
```

### 3B) Showing all possible matches

Implement `show_possible_matches(my_word)`:
- `my_word`: a guessed word, possibly containing `_`'s

Prints all words in `wordlist` that match `my_word`. Prints `"No matches found"` if there are none.

**Example usage:**
```python
>>> show_possible_matches("t_ _ t")
tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit

>>> show_possible_matches("abbbb_ ")
No matches found

>>> show_possible_matches("a_ pl_ ")
ample amply
```

### 3C) Hangman with hints

Replicate your `hangman` code as the body of `hangman_with_hints`, with one addition: if the user guesses `*`, print all matching words using `show_possible_matches`. The user should not lose a guess for guessing `*`.

Comment out the lines used to play the original game:
```python
secret_word = choose_word(wordlist)
hangman(secret_word)
```

And uncomment the lines for the hints version:
```python
#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)
```

**Sample output** (guessing `*` should follow this pattern; all other output follows the rules from Problem 3):

```
Loading word list from file...
   55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 5 letters long.
--------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: a_ _ _ _
--------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: l
Good guess: a_ _ l_
--------
You have 6 guesses left.
Available letters: bcdefghijkmnopqrstuvwxyz
Please guess a letter: *
Possible word matches are:
addle adult agile aisle amble ample amply amyls angle ankle apple
apply aptly arils atilt
--------
You have 6 guesses left.
Available letters: bcdefghijkmnopqrstuvwxyz
Please guess a letter: e
Good guess: a_ _ le
--------
```
