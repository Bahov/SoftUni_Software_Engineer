string_input = input()

all_digits = [symbol for symbol in string_input if symbol.isdigit()]
all_letters = [symbol for symbol in string_input if symbol.isalpha()]
other = [symbol for symbol in string_input if symbol not in all_letters + all_digits]
all_digits = list(map(int, all_digits))

print(''.join(str(digit) for digit in all_digits))
print(''.join(all_letters))
print(''.join(other))