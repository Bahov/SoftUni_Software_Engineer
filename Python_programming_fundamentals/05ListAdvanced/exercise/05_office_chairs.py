number_of_rooms = int(input())

visitors = 0
chairs = 0
insufficient = False
total_chairs = 0
total_visitors = 0

for room in range(1, number_of_rooms + 1):
    input_list = input().split(' ')
    current_chairs = input_list[0].count('X')
    current_visitors = int(input_list[1])
    if current_chairs < current_visitors:
        print(f'{current_visitors - current_chairs} more chairs needed in room {room}')
        insufficient = True
    total_visitors += current_visitors
    total_chairs += current_chairs


if not insufficient:
    print(f'Game On, {total_chairs - total_visitors} free chairs left')
    
