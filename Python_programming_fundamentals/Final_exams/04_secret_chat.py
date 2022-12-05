message = input()

command = input()

while command != 'Reveal':
    command_list = command.split(':|:')
    action = command_list[0]
    if action == 'InsertSpace':
        index = int(command_list[1])
        left_part = message[:index]
        right_part = message[index:]
        message = left_part + ' ' + right_part
        print(message)
    elif action == 'Reverse':
        substring = command_list[1]
        if substring in message:
            start_index = int(message.find(substring))
            end_index = start_index + len(substring)
            left_part = message[:start_index]
            right_part = message[end_index:]
            message = left_part + right_part + substring[::-1]
            print(message)
        else:
            print('error')
    elif action == 'ChangeAll':
        substring = command_list[1]
        replacement = command_list[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()

print(f'You have a new text message: {message}')