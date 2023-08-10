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

def user_guess(word):
    pass
    # while counter > 0:
    #     if counter! = 
    # take in user input and compare it the word, will return if it was wrong or the correct letter



def play_game():
    random_word = select_word('short_list.txt')
    print(random_word)
    guess_letters = []
    print(display_secret_board(random_word, guess_letters))


if __name__ == "__main__":
    play_game()
