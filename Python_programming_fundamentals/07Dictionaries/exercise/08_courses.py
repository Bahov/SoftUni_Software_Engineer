command = input()

register = {}

while command != 'end':
    command_list = command.split(' : ')
    if command_list[0] not in register.keys():
        register[command_list[0]] = [command_list[1]]
    else:
        register[command_list[0]].append(command_list[1])
    command = input()

for course,students in register.items():
    print(f"{course}: {len(students)}")
    print('\n'.join('-- ' + student for student in students))