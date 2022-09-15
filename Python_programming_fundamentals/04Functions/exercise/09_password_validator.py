password = input()

def out_of_range(password):
    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        return True

def fail_letter_digit(password):
    for index, char in enumerate(password):
        if not char.isalpha() and not char.isdigit():
            print('Password must consist only of letters and digits')
            return True

def insufficient_digit(password):
    digit_count = 0
    for index, char in enumerate(password):
        if char.isdigit():
            digit_count += 1
    if digit_count < 2:
        print('Password must have at least 2 digits')
        return True

check_list = [out_of_range(password), insufficient_digit(password), fail_letter_digit(password)]
if not all(check_list):
    print('Password is valid')