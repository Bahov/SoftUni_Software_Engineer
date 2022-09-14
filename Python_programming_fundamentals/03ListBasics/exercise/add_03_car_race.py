track_list = input().split(' ')

number_of_steps = len(track_list) // 2

left_list = track_list[:number_of_steps]
time_left = 0

right_list = track_list[number_of_steps + 1:]
right_list.reverse()
time_right = 0

for step in range(0, number_of_steps):

    if int(left_list[step]) == 0:
        time_left *= 0.8
    else:
        time_left += int(left_list[step])

    if int(right_list[step]) == 0:
        time_right *= 0.8
    else:
        time_right += int(right_list[step])

if time_left < time_right:
    print(f'The winner is left with total time: {time_left:.1f}')
else:
    print(f'The winner is right with total time: {time_right:.1f}')