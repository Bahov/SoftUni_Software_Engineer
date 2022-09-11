

string_input = input()

repeated_string = ''
while string_input != 'End':
    if string_input == 'SoftUni':
        pass
    else:
        for index in range(len(string_input)):
            repeated_string = repeated_string + string_input[index] * 2
        print(repeated_string)
    repeated_string = ''
    string_input = input()