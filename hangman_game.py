import string
import random


def main_game():
    print("\nThe game started!\n")
    words = ['cat', 'dog', 'mouse', 'elephant', 'deer', 'chicken']
    r_open = random.choice(words)
    lst_r_open = list(r_open)

    lives = 3
    r_closed = '*' * len(r_open)

    while lives > -1 and not r_closed == r_open:
        print("Word: " + r_closed)
        print("Lives left: " + str(lives))
        print("------------------------------")

        letters = list(string.ascii_lowercase)
        letter = input("Choose a letter: ")

        if letter in letters:
            if letter in lst_r_open:
                r_closed = update_r_closed(r_open, r_closed, letter)
                print("You're right, " + letter + " is exist.")
            else:
                if lives == 0:
                    print("Game Over")
                    restart = input("You lost! Play again ?(y/n)")
                    if restart == "y":
                        main_game()
                    else:
                        exit()

                elif lives > -1:
                    lives -= 1
                    print("You're wrong, " + letter + " isn't  exist.")
        else:
            print("Choose one letter!")

    if r_closed == r_open:
        restart = input("You won! Play again ?(y/n)")
        if restart == "y":
            main_game()
        else:
            exit()


def update_r_closed(secret, cur_dash, rec_guess):
    result = ""

    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result += rec_guess

        else:
            result += cur_dash[i]

    return result


main_game()
