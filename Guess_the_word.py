
"""
                            -------------- Short Reflection ---------------
    One design choice I changed mid-way was initializing my wins and losses lists in the top-level
code. I planned to initialize these lists in the function keep_score() but then I realized that
my data is being reset each game and I need these lists to live in a global area. I validated input
by implementing tries and excepts every time there calls for user input. If I had more time, I would
add graphics to the game because I think it would take the game to a whole new level.

                                -------------- Pseudocode ---------------
Print to the user: 'This is a word-guessing game. The computer chooses a secret word from a
    specific category; the player guesses letters. Correct guesses reveal letters; incorrect guesses
    reduce the number of tries. By typing "hint", the player can request to reveal one random
    unguessed letter(costs 2 tries). The game ends when the player reveals the whole word or
    runs out of tries.'

Import built-in random module
Initialize user_guess to an integer, 0
Initialize your_wins to a list, [0]
Initialize your_losses to a list, [0]

Function secret_word()
    Ask user to choose a category: (animals, foods, colors)
    Validate the user choice
    If user chooses animals
        Store a small in-code list of at least 20 animals
    If user chooses foods
        Store a small in-code list of at least 20 foods
    If user chooses sports
        Store a small in-code list of at least 20 colors
    Pick one random word from the category
    Return secret_word
End function

Function initialize_revealed()
    Set the secret_word to revealed, a set of underscores instead of letters
    Return revealed
End function

Function ask_and_validate_guess()
    While true
        Try
            Ask user to enter a character
            If user_input is 'hint
                Break out of loop
            If guess is blank
                Raise ValueError
            If guess is not in the range a-z
                Raise ValueError
            If characters in guess is greater than 1
                Raise ValueError
            Otherwise
                Break out of loop
        Except ValueError
            Ignore and reprompt
        If the user_guess is not 'hint'
            Store in list of already guessed letters

        Add a counter to the secret word
        If the user_guess is in the secret_word and unrevealed
            Place the user_guess in the word and reveal to user

        Done is True
        Add a counter to the secret word
            If the guess is not in the secret word
                Done is False

        Return revealed word
End function

Function keep_score()
    If Done is True
        Add a win to the list of wins
    Otherwise
        Add a loss to the list of losses
    Print list of wins and losses
    Return list of wins and losses
End function

Function play_again()
    While True
        Ask user if they want to play again
        Validate the user input
        If the answer is yes
            Call the game
        If the answer is no
            Break out of the loop
    Print a friendly message to the user
End function

Function limit_tries()
    Set the remaining_tries to 6
    While true
        Call the function ask_and_validate_guess(sw, r, guessed_letters)
        If Done is True
            Print friendly message to the user
            Break out of loop
        If the remaining_tries is 0
        Print a friendly message to the user
            Print helpful message to user
            Break out of loop
        If user guess is 'hint'
            Reveal a random unguessed letter
            Subtract 2 from remaining_tries
        If user guess is not in the ssecret word
            Subtract 1 from remaining_tries

        Print remaining_tries and list of already guessed letters
    Return remaining_tries, done
End function

"""
print("""This is a word-guessing game.
The computer chooses a secret word from a specific category; the player guesses letters.
Correct guesses reveal letters; incorrect guesses reduce the number of tries.
By typing 'hint', the player can request to reveal one random unguessed letter(costs 2 tries).
The game ends when the player reveals the whole word or runs out of tries.""")

import random
user_guess = 0   # The character that the user inputs
your_wins = [0]   # A list that keeps track of the user's wins
your_losses = [0]   # A list that keeps track of the user's losses

def secret_word():
    guessed_letters = []   # A list that keeps track of the user's guessed letters

    while True:   # Read until user chooses a valid category
        categories = ['animals', 'foods', 'colors']   # A list of the three possible word box categories
        category_choice = input("Choose a category: (animals, foods, colors): ").strip().lower()
        if category_choice in categories:
            if category_choice == 'animals':
                # A list of the possible secret words in the animal category
                word_box = ['cat', 'dog', 'bird', 'tiger', 'lion', 'monkey', 'bear', 'panda',
                            'horse', 'donkey', 'cow', 'snake', 'turtle', 'sheep', 'fox',
                            'bunny', 'hamster', 'chicken', 'goat', 'zebra']
            if category_choice == 'foods':
                # A list of the possible secret words in the food category
                word_box = ['pizza', 'pasta', 'fries', 'chicken', 'cucumber', 'bread',
                            'cupcake', 'cheese', 'strawberry', 'mango', 'rice', 'apple',
                            'donut', 'jam', 'pretzel', 'crackers', 'chips', 'yogurt',
                            'oatmeal', 'soup']
            if category_choice == 'colors':
                # A list of the possible secret words in the color category
                word_box = ['red', 'yellow', 'blue', 'orange', 'green', 'purple',
                            'white', 'black', 'grey', 'pink', 'gold', 'silver', 'teal',
                            'violet', 'brown', 'navy', 'magenta', 'olive', 'coral', 'cyan']
            break
        else:
            print("Invalid choice. Please try again.")
            continue

    secret_word = random.choice(word_box)   # Assigns a random word in the word box as the secret word
    return secret_word, guessed_letters

def initialize_revealed(sw):
    revealed = ['_'] * len(sw)   # Repeats a pattern 'underscore' by however many characters
                                 # there are in the secret word
    return revealed

def ask_and_validate_guess(sw, r, guessed_letters):
    while True:   # Read until user guesses a valid character
        try:
            user_guess = input("Guess a character: ").strip().lower()
            if user_guess == 'hint':   # Allows the user to input 'hint' to be dealt with later
                break
            if user_guess == '':
                raise ValueError
            if not user_guess.isalpha():
                raise ValueError
            if len(user_guess) > 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid guess. Please try again.")
            continue

    if user_guess != 'hint':
        guessed_letters.append(user_guess) # Creates a word box of previously guessed letters for the user

    for i, ch in enumerate(sw):   # Reads each character in the secret word and find it's position
        if ch == user_guess and r[i] == "_":   # If the user guess is in the secret word
            r[i] = user_guess   # Add the character to the revealed word

    done = True # Initializes done to true and done becomes false if the user guess is not in the secret word
    for i, ch in enumerate(sw):
        if r[i] != ch:
            done = False

    return r, user_guess, done, guessed_letters

def keep_score(done, remaining_tries): #(user_guess, revealed_word, remaining_tries):
    if done:   # If all the characters in the revealed word, comprised of user guesses, matches the
               # secret word
        your_wins[0] += 1
    else:
        your_losses[0] +=1

    print(f"Wins: {your_wins} Vs Losses: {your_losses}")
    return your_wins, your_losses

def play_again():
    while True:   # Read until user selects a valid choice, yes or no.
        try:
            ask_replay = input("Would you like to play again? (y/n): ").strip().lower()
            if ask_replay == 'y':
                main()   # Start the game over
            if ask_replay == 'n':
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

    print("Thank you for playing!")

def limit_tries(r, sw, user_guess, guessed_letters):
    remaining_tries = 6   # Assigns the users maximum tries as six

    while True:   # Read until the user guessed the word or runs out of tries.
        r, user_guess, done, guessed_letters = ask_and_validate_guess(sw, r, guessed_letters)
        if done:
            print(f"You guessed the word: {sw}!")
            print("Game over!")
            break
        if remaining_tries == 0:
            print("Game over!")
            break
        elif user_guess == 'hint':
            underscores = []
            for i, ch in enumerate(sw):   # Reads each character in the revealed word and makes a
                                          # list of all the unguessed characters
                if  r[i] == "_":
                    underscores.append(i)

            h = random.choice(underscores)
            for i, ch in enumerate(sw):   # Reveals a random unguessed character
                if  i == h:
                    r[i] = ch

            remaining_tries -= 2
        elif user_guess not in r:
            remaining_tries -= 1

        print(r)
        print(f"You have {remaining_tries} tries remaining.")
        print(f"You already guessed: {guessed_letters}")
    return remaining_tries, done

def main():
    sw, guessed_letters = secret_word()
    r = initialize_revealed(sw)
    remaining_tries, done = limit_tries(r, sw, user_guess, guessed_letters)
    your_wins, your_losses = keep_score(done, remaining_tries)
    play_again()

main()

