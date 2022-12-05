initial_string = input()

command = input()

while command != 'End':
    command_list = command.split(' ')
    action = command_list[0]
    if action == 'Translate':
        character = command_list[1]
        replacement = command_list[2]
        initial_string = initial_string.replace(character, replacement)
        print(initial_string)
    elif action == 'Includes':
        substring = command_list[1]
        if substring in initial_string:
            print('True')
        else:
            print('False')
    elif action == 'Start':
        substring = command_list[1]
        len_substring = len(substring)
        check_part = initial_string[:len_substring]
        if substring == check_part:
            print('True')
        else:
            print('False')
    elif action == "Lowercase":
        initial_string = initial_string.lower()
        print(initial_string)
    elif action == 'FindIndex':
        character = command_list[1]
        last_occurence = initial_string.rfind(character)
        print(last_occurence)
    elif action == 'Remove':
        start_index = int(command_list[1])
        count_chars = int(command_list[2])
        use_index = start_index + count_chars
        initial_string = initial_string[:start_index] + initial_string[use_index:]
        print(initial_string)
    command = input() 