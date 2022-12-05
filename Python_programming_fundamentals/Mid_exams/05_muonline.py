health = 100
bitcoin = 0

rooms = input().split('|')
room_counter = 0
is_dead = False

for room in rooms:
    room_list = room.split(' ')
    command = room_list[0]
    number = int(room_list[1])
    room_counter += 1
    if command == 'potion':
        if health == 100:
            print('You healed for 0 hp.')
            print('Current health: 100 hp.')
        else:
            if 100 - health > number:
                health += number
                print(f'You healed for {number} hp.')
                print(f'Current health: {health} hp.')
            else:
                print(f'You healed for {100 - health} hp.')
                health = 100
                print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoin += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            is_dead = True
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room_counter}')
    if is_dead:
        break

if room_counter == len(rooms) and not is_dead:
    print("You've made it!")
    print(f'Bitcoins: {bitcoin}')
    print(f'Health: {health}')
