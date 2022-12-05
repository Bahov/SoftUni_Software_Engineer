line = list(map(int, input().split('@')))

command = input()
current_index = 0

while command != 'Love!':
    command_list = command.split(' ')
    jump_length = int(command_list[1])
    current_index += jump_length
    if current_index > len(line) - 1:
        current_index = 0
    if line[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        line[current_index] -= 2
        if line[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_index}.")
remaining_places = [place for place in line if place > 0]
if len(remaining_places) > 0:
    print(f"Cupid has failed {len(remaining_places)} places.")
else:
    print('Mission was successful.')    