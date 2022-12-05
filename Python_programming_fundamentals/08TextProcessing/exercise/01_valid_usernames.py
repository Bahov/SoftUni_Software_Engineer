from curses.ascii import isalpha


usernames = input().split(', ')

is_valid = True

for name in usernames:
    if 3 <= len(name) <= 16:
        for symbol in name:
            if not symbol.isalpha() and not symbol.isdigit() and symbol not in ('-','_'):
                is_valid = False
        if is_valid:
            print(name)
    is_valid = True