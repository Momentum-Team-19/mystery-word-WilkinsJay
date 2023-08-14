import random


def select_word(filename):
    with open(filename) as file:
        file = file.read()
    words_list = file.split()
    random_word = random.choice(words_list)
    return random_word
    # take in a file and return a word in list, selected at random


def display_secret_board(word, guess_letters):
    chosen_word = ''
    for letter in word: 
        if letter in guess_letters:
            chosen_word += letter
        else:
            chosen_word += '_'
    return chosen_word
    # this function will display as underscores or a letter that were guessed correctly


def user_guess(counter):
    while counter > 0:
        if counter != 0:
            print(f'You have {counter} guesses left')
        guess = input('guess a letter: ').lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter only 1 letter')
        else:
            return guess
    # take in user input and compare it the word, will return if it was wrong or the correct letter


def display_game_over():
    print('Game over!')
    replay = input('Play again? (y/n): ')
    return replay.lower() == 'y'


def restart_game():
    replay = display_game_over()
    if replay:
        play_game()
    else:
        exit()


def play_game():
    random_word = select_word('short_list.txt')
    guess_letters = []
    counter = 8
    while counter > 0:
        display = display_secret_board(random_word, guess_letters)
        print(display)
        if '_' not in display:
            print('You got it correct!', random_word)
            break
        guess = user_guess(counter)
        guess_letters.append(guess)
        if guess not in random_word:
            counter -= 1
    else:
        print('Better luck next time 🤓')
    print(random_word)
    print(display_secret_board(random_word, guess_letters))
    restart_game()


if __name__ == "__main__":
    play_game()
