import re
import string

from wordfreq import get_frequency_dict

# ==== Functions =======================================
def reverseShift(ciphertext: str, shift: int):

    # Gets the alphabet, in lowercase.
    alphabet = string.ascii_lowercase
    # shifts the alphabet over by "shift"
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]
    # creates a translation table that maps each letter in alphabet to the shifted alphabet
    table = str.maketrans(alphabet, shifted_alphabet)

    # performs the shifting using the table.
    result = ciphertext.translate(table)
    return result


# ==== Main ============================================

# This only supports english currently, this is a list of 'common' english words
enWords = get_frequency_dict('en', wordlist='small')

ceaserText = input("Ceaser cipher text: ").lower()

matchCount = 0
for i in range(0, 26):

    # reverses the shift by I amount
    shiftedText = reverseShift(ceaserText, i)
    # get a list of each word, to check against the dictionary.
    shiftedWords = shiftedText.split()

    # cleans each word, so its only a-z
    for j in shiftedWords:
        j = re.sub(r'[^a-z]', '', j)
        if j in enWords:
            matchCount += 1

    if matchCount >= len(shiftedWords) * 0.5:
        print("Match found at shift ", i, "\nResult: ", shiftedText)

    matchCount = 0

