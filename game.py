from random import choice
from math import trunc


valid_letters = ['R', 'Y', 'G', 'B', 'I', 'V']
len_of_code = 4

def generate_code():
    code_for_guess = []
    for i in range(len_of_code):
      code_for_guess.append(choice(valid_letters))
    return code_for_guess

# def validate_guess(guess):
#     if len(guess) == len_of_code:
#         guess = [letter.upper() for letter in guess]
#         check_letter = all(letter in valid_letters for letter in guess)
#         return check_letter
#     else:
#         return False

def validate_guess(guess):
    if len(guess) == len_of_code:
        for letter in guess:
            if letter.upper() not in valid_letters:
                return False
        return True
    return False

def color_count(guess, code):
    correct_colors = 0
    util_code = code[:]
    for color in guess:
        if color in util_code:
            correct_colors += 1
            util_code.remove(color)
    return correct_colors

def correct_pos_and_color(guess, code):
    correct_colors_and_positions = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:
            correct_colors_and_positions += 1
    return correct_colors_and_positions

def check_guess(guess, code):
    return correct_pos_and_color(guess, code), color_count(guess, code) - correct_pos_and_color(guess, code)

def check_win_or_lose(guess, code, num_guesses):
    if guess == code and num_guesses <= 8:
        return True
    elif num_guesses > 8:
        return False

def get_win_percentage(wins, plays):
    if wins == 0 or plays == 0:
        return 0
    else:
        return trunc(wins/(plays/100))

def format_guess_stats(guess_stats):
    guess_stats_list = []
    for i in range(8):
        if guess_stats.get(i+1) != None:
            guess_stats_list.append(guess_stats[i+1] * "X")
        else:
            guess_stats_list.append('')
    return guess_stats_list
