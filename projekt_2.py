# Úvod

'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Diana Stiborová
email: stiborovadiana@seznam.cz
'''

# Importování knihoven.

import sys
import random

# Generovaní hádaného čísla.
# Číšlo nesmí začínat 0 a nesmí se opakovat.

def generate_number():
    number = ""
    while len(number) < 4:
        random_number = str(random.randint(1, 9))

        # Kontrola zda číslo random_number není v řetězci number.

        if random_number not in number:
            number = number + random_number
    return number

# Vyhodnocení čísla od uživatele

def check_numbers(user_numbers, secret_numbers):
    bulls = 0
    cows = 0
    index = 0
    for user_number in user_numbers:

        # Pokud hráč uhodl číslo na správné pozici = bulls.

        if user_numbers[index] == secret_numbers[index]:
            bulls += 1

        # Pokud hráč uhodl číslo na nesprávné pozici = cows.

        elif user_number in secret_numbers:
            cows += 1

        # Po každém cyklu se připočítá index.

        index += 1
    return bulls, cows

# Jednotné nebo množné číslo u bull/bulls a cow/cows.

def bulls_and_cows_names(bulls, cows):
    if bulls == 1:
        bulls_name = "bull"
    else:
        bulls_name = "bulls"

    if cows == 1:
        cows_name = "cow"
    else:
        cows_name = "cows"

    return f"{bulls} {bulls_name}, {cows} {cows_name}"

# Hlavní část programu

def main():

    # Generování tajného čísla.

    secret_num = generate_number()

    # Pozdravení hráče

    hello = """
    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play bulls and cows game.
    -----------------------------------------------
    """
    prompt = """
    Enter a number:
    -----------------------------------------------
    """
    print(hello)


    # Zadání uživatelského čísla.

    try_number = 0
    while True:
        user_num = input(prompt)

    # Kontrola čísla.

        if len(user_num) != 4 or not user_num.isdigit():
            print("Wrong input. You must enter 4-digit unique number!")
        else:

            # Vyhodnocení čísla.

            bulls, cows = check_numbers(user_num, secret_num)

            # Pokud hráč vyhrál

            if bulls == 4:
                print(f"Congratulations! You guessed the number in {try_number + 1} tries.")

                # Pokud bude chtít hráč hrát znovu.

                play_again = input("Do you want to play again? Please enter (y/n): ")
                if play_again.lower() == "y":
                    secret_num = generate_number()
                    try_number = 0
                else:
                    sys.exit()
            else:
                print(bulls_and_cows_names(bulls, cows))
                try_number += 1

# Spuštění funkce.

if __name__ == '__main__':
    main()






