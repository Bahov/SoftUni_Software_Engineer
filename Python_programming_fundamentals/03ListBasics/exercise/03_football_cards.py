a_team = ["A-" + str(i) for i in range(1, 12)]
b_team = ["B-" + str(i) for i in range(1, 12)]

input_string = input().split(' ')

game_terminated = False

for i in input_string:

    if i in a_team:
        a_team.remove(i)
    elif i in b_team:
        b_team.remove(i)
    
    if len(a_team) < 7 or len(b_team) < 7:
        game_terminated = True
        break 

print(f'Team A - {len(a_team)}; Team B - {len(b_team)}')
if game_terminated:
    print('Game was terminated')
