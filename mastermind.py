from game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, \
    get_win_percentage, format_guess_stats
import time


# These functions allow you to print a string s in the stated colors. Using them is NOT required
def print_red(s):
    return '\033[31m' + s + '\033[0m'


def print_yellow(s):
    return '\033[33m' + s + '\033[0m'


def print_green(s):
    return '\033[32m' + s + '\033[0m'


def print_blue(s):
    return '\033[36m' + s + '\033[0m'


def print_indigo(s):
    return '\033[34m' + s + '\033[0m'


def print_violet(s):
    return '\033[35m' + s + '\033[0m'


# This function converts the player's guess string into a list
def split(guess):
    return [char for char in guess]


# This function prints the statistical data
def print_statistics(plays, wins, guess_stats):
    print('\nSTATISTICS')
    print(f'Games Played: {plays}')
    print(f'Win %: {get_win_percentage(wins, plays)}')
    print('Guess Distribution:')
    guess_distribution = format_guess_stats(guess_stats)
    for i, v in enumerate(guess_distribution):
        print(str(i + 1) + '| ' + v)


def mastermind():
    play_loop = 'y'
    max_guesses = 8
    plays = 0
    wins = 0
    guess_stats = {}

    print('Welcome to Mastermind!')

    while play_loop == 'y':
        print('Generating a new code...')
        code = generate_code()
        guesses = 0
        guess = ''
        # print generated code for debugging
        # print(code)
        time.sleep(2)
        print('New code generated: ****')
        time.sleep(2)
        print('\nGuess the code! \n'
              'You should guess four characters \n'
              'Each character in the code is one of the following letters: R, Y, G, B, I, V')

        while correct_pos_and_color(guess, code) != len(code) and guesses < max_guesses:
            guess = input('Guess the code: ').upper()
            guess = split(guess)

            while not validate_guess(guess):
                print('\nCheck your guess! \n'
                      'You should guess four characters \n'
                      'Each character in the code is one of the following letters: R, Y, G, B, I, V')
                guess = input('Guess the code: ').upper()
                guess = split(guess)

            else:
                colorful_guess = ''
                for char in guess:
                    if char == 'R':
                        colorful_guess += print_red(char)
                    elif char == 'Y':
                        colorful_guess += print_yellow(char)
                    elif char == 'G':
                        colorful_guess += print_green(char)
                    elif char == 'B':
                        colorful_guess += print_blue(char)
                    elif char == 'I':
                        colorful_guess += print_indigo(char)
                    elif char == 'V':
                        colorful_guess += print_violet(char)
                print(f'\nYou guessed: {colorful_guess}')
                guesses += 1

                if check_win_or_lose(guess, code, guesses):
                    print('Congratulations! You guessed the secret code!')
                    wins += 1
                    plays += 1
                    if guesses not in guess_stats:
                        guess_stats[guesses] = 1
                    else:
                        guess_stats[guesses] += 1
                    break
                else:
                    print(check_guess(guess, code))
                    if max_guesses - guesses > 1:
                        print(f'You have {max_guesses - guesses} more guesses')
                    elif max_guesses - guesses == 1:
                        print(f'You have {max_guesses - guesses} more guess')
                    else:
                        print("You don't have more guesses")
                        print('You lost 😥 Better luck next time!')
                        plays += 1

        print_statistics(plays, wins, guess_stats)

        print('\nShould we play another round?')
        print('Enter y to replay, any other character to exit: ')
        play_loop = input('user input: ').lower()
    return print('\nThank you for the game! See you next time!')


mastermind()
