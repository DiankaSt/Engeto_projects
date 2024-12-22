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
garpike and stingray are also present.'''
]

data = {'user': 'passport',
        'bob': '123',
        'ann': 'pass123',
        'mike': 'password123',
         'liz': 'pass123',
        }
separate = '=' * 40
number_text = list(range(0, len(TEXTS)))

username = input('Please enter your user name:  ')
password = input('Please enter your password:  ')
# Control of your user name and password:
if data.get(username) == password:
    print(f'username: {username}')
    print(f'password: {password}')
else:
    print('Your username or password is incorrect.')
    exit()
print(separate)
print(f'Welcome to the app, {username}')
print(f'We have {len(number_text)} texts to be analyzed')
print(separate)
while True:
    text_selection = input(f'Enter a number of text. 1 and {len(TEXTS)} to select: ')
# Control of text selection:
    if not text_selection.isdigit():
        print("Input is not number, but text.")
    else:
        text_selection = int(text_selection) - 1


    if text_selection in number_text:
        print(f'You have selected the number of your text: {text_selection + 1}')
        break
    else:
        print('You have made an error. The application will be closed.')

# Counting number of words:
print(separate)

only_words = TEXTS[text_selection].replace(".", "").replace(",", "").replace(";", "")
word_list = only_words.split()
print('There are', len(word_list), 'words in the selected text.')
text_split_words = (TEXTS[text_selection]).split()

titlecase_words = 0
for i in text_split_words:
    if i[0].isupper():

# Counting of titlecase words:
        titlecase_words = titlecase_words + 1
print('There are', titlecase_words, 'titlecase words.')

# Counting of uppercase words:
uppercase_words = 0

for i in text_split_words:
    if i.isupper():
        uppercase_words += 1
print('There are', uppercase_words, 'uppercase words.')

# Counting of lowercase words:
lowercase_words = 0
for i in text_split_words:
    if i.islower():
        lowercase_words += 1
print('There are', lowercase_words, 'lowercase words.')

# Counting of numeric strings:
count_num_words = 0
for i in text_split_words:
    if i.isdigit():
        count_num_words += 1
print('There are', count_num_words, 'numeric strings.')

# Counting the sum of all numbers:
total_sum = 0
for line in text_split_words:
    if line.strip().isdigit():
        total_sum += int(line)
print('The sum of all the numbers', total_sum)
print(separate)


dict_words = {}
for word in text_split_words:
    word_len = len(word)
    if word_len not in dict_words.keys():
        dict_words[word_len] = 1
    else:
        dict_words[word_len] += 1

# The graph of frequency of the words:
print('LEN| OCCURENCES   | NR.')
max_star_count = 12

sorted_keys = sorted(dict_words, key=dict_words.get)

sorted_keys.sort()
for key in sorted_keys:

    str_key = str(key)
    if len(str_key) == 1:
        str_key = " " + str_key
    stars = "*" * dict_words[key]
    count = str(dict_words[key])

    part_star_count = max_star_count - dict_words[key]
    star_fill = " " * part_star_count

    print(f"{str_key} | {stars}{star_fill} | {count}")
