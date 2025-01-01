'''
projekt_1.py: Diana Stiborová
email: stiborovadiana@seznam.cz
'''

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

# Dictionary containing users and their passwords
data = {'user': 'passport',
        'bob': '123',
        'ann': 'pass123',
        'mike': 'password123',
        'liz': 'pass123'}

separator = '=' * 40

# User and password verification
username = input('Please enter your username: ')
password = input('Please enter your password: ')
if data.get(username) != password:
    print('Your username or password is incorrect.')
    exit()

print(separator)
print(f'Welcome to the app, {username}')
print(f'We have {len(TEXTS)} texts to be analyzed.')
print(separator)

# Selection of texts
while True:
    text_selection = input(f'Enter a number between 1 and {len(TEXTS)} to select: ')
    if text_selection.isdigit() and 1 <= int(text_selection) <= len(TEXTS):
        text_selection = int(text_selection) - 1
        print(f'You have selected text number {text_selection + 1}.')
        break
    else:
        print('Invalid input. The application will be closed.')
        exit()

# Text analysis
selected_text = TEXTS[text_selection]
words = [word.strip(".,;") for word in selected_text.split()]

# Count of word categories
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = []
word_lengths = {}

for word in words:
    if word.istitle():  # Check for title words
        titlecase_words += 1
    if word.isupper() and word.isalpha():  # Check for uppercase words
        uppercase_words += 1
    if word.islower():  # Check for lowercase words
        lowercase_words += 1
    if word.isdigit():  # Check for numeric strings
        numeric_strings.append(int(word))
    # Count occurrences of word lengths
    word_len = len(word)
    word_lengths[word_len] = word_lengths.get(word_len, 0) + 1

# Display analysis results
total_sum = sum(numeric_strings)  # Sum all numeric values
print(separator)
print(f'There are {len(words)} words in the selected text.')
print(f'There are {titlecase_words} titlecase words.')
print(f'There are {uppercase_words} uppercase words.')
print(f'There are {lowercase_words} lowercase words.')
print(f'There are {len(numeric_strings)} numeric strings.')
print(f'The sum of all the numbers is {total_sum}')
print(separator)

# Display word length as a graph
print('LEN | OCCURRENCES  | NR.')
print(separator)
max_stars = 12
for length, count in sorted(word_lengths.items()):
    stars = '*' * count
    stars = stars.ljust(max_stars)
    print(f'{length:>3} | {stars} | {count:>2}')

