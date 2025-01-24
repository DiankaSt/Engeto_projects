# Úvod
'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Diana Stiborová
email: stiborovadiana@seznam.cz
'''

# Importování knihoven.
import sys
import random

# Generování hádaného čísla (nesmí začínat 0 a čísla se nesmí opakovat)
def generate_number():
    number = str(random.randint(1, 9))
    while len(number) < 4:
        digit = str(random.randint(0, 9))
        if digit not in number:
            number += digit
    return number


# Vyhodnocení čísla od uživatele
def check_numbers(user_numbers, secret_numbers):
    bulls = 0
    cows = 0

    for i in range(4):
        if user_numbers[i] == secret_numbers[i]:
            bulls += 1  # Správné číslo na správné pozici
        elif user_numbers[i] in secret_numbers:
            cows += 1  # Správné číslo na špatné pozici
    return bulls, cows


# Jednotné nebo množné číslo u bulls and cows
def bulls_and_cows_names(bulls, cows):
    bulls_name = "bull" if bulls == 1 else "bulls"
    cows_name = "cow" if cows == 1 else "cows"
    return f"{bulls} {bulls_name}, {cows} {cows_name}"

# Ověř správnost čísla
def is_valid_number(user_num):
    return len(user_num) == 4 and user_num.isdigit() and user_num[0] != "0" and len(set(user_num)) == 4


# Hlavní část programu
def main():
    secret_num = generate_number()
    print("""
    Hi there!
    -----------------------------------------------
    I've generated a random 4-digit number for you.
    Let's play bulls and cows game.
    -----------------------------------------------
    """)
    try_number = 0
    while True:
        user_num = input("Enter a number: ")

        if not is_valid_number(user_num):
            print("Wrong input. You must enter a 4-digit unique number that doesn't start with 0!")
            continue

        try_number += 1
        bulls, cows = check_numbers(user_num, secret_num)

        if bulls == 4:
            print(f"Congratulations! You guessed the number in {try_number} tries.")
            if input("Do you want to play again? (y/n): ").lower() == "y":
                secret_num = generate_number()
                try_number = 0
            else:
                sys.exit()
        else:
            print(bulls_and_cows_names(bulls, cows))


if __name__ == '__main__':
    main()
