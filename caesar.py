def alphabet_position(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i == letter:
            return alphabet.index(i)

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    char_num = alphabet_position(char)
    new_num = char_num + rot
    if new_num >25:
        new_num = (new_num % 26)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_char = alphabet[new_num]
    if char == char.upper():
        return new_char.upper()
    else:
        return new_char.lower()

def encrypt(text, rot):
    new_str = ""
    for i in text:
        new_char = rotate_character(i, rot)
        new_str += new_char
    return new_str
