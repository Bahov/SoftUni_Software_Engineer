first_char = input()
second_char = input()

def chars_from_ascii(first_char, second_char):
    for index in range(ord(first_char) + 1, ord(second_char)):
        print(chr(index), end = ' ')

chars_from_ascii(first_char, second_char)