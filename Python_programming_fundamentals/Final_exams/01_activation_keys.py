
raw_key = input()

command = input()

while command != 'Generate':
    command_list = command.split('>>>')
    operation = command_list[0]
    if operation == 'Contains':
        substring = command_list[1]
        if substring in raw_key:
            print(f'{raw_key} contains {substring}')
        else:
            print('Substring not found!')
    elif operation == 'Flip':
        suboperation = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])
        rep_string = raw_key[start_index:end_index]
        if suboperation == 'Upper':
            raw_key = raw_key.replace(rep_string, rep_string.upper())
        elif suboperation == 'Lower':
            raw_key = raw_key.replace(rep_string, rep_string.lower())
        print(raw_key)
    elif operation == 'Slice':
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)
    command = input()

print(f'Your activation key is: {raw_key}')