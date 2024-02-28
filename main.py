import re
import os

morse_codes = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '  '  # separator between words
}

banner = '''
 __  __                        ____          _         ____                          _            
|  \/  | ___  _ __ ___  ___   / ___|___   __| | ___   / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
| |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \ | |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/ | |__| (_) | | | \ V /  __/ |  | ||  __/ |   
|_|  |_|\___/|_|  |___/\___|  \____\___/ \__,_|\___|  \____\___/|_| |_|\_/ \___|_|   \__\___|_|   
 
'''


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def words_to_morse():
    valid = True
    convertedMessage = ''
    message = input('What word should be converted?: ').upper()
    for letter in message:
        if letter in morse_codes:
            convertedMessage += ' ' + morse_codes[letter]
        else:
            valid = False # invalid if one symbol could not be converted
    if valid:
        return convertedMessage
    else:
        return 'Invalid Input...'
     
def morse_to_words():
    valid = True
    convertedMessage = ''
    message = input('What piece of morse code should be converted? (seperate symbols by 1 space and words by 2 spaces): ')
    wordList = re.split(r'\s{2,}', message)
    counter = 0
    for word in wordList:
        for letter in word.split():
            counter += 1  # counts number of morse code items input
            for symbol, code in morse_codes.items():
                if letter == code:
                    convertedMessage += symbol.lower()
        convertedMessage += ' '
    letters_only = convertedMessage.replace(" ","")
    if counter != len(letters_only): # invalid, if one morse code item could not be converted
        valid = False
    if valid:
        return convertedMessage
    else:
        return 'Invalid Input...'

def main():
    cls()
    print(banner)
    mode = input('Do you want to decode a word (1) or encode morse code (2)?: ')
    if mode == '1':
        print(words_to_morse())
    elif mode == '2':
        print(morse_to_words())
    else:
        print(f'{mode} is not a valid choice...')
        main()

if __name__ == main():
    main()