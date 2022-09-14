start_list = input().split('|')

energy = 100
coins = 100
temp_list = []
gained_energy = 0
gained_coins = 0
is_closed = False

for j in range(len(start_list)):
    temp_list.append(str(start_list[j]).split('-'))
    if temp_list[j][0] == 'rest':
        temp_energy = energy
        energy += int(temp_list[j][1])
        if energy >= 100:
            energy = 100
            gained_energy = energy - temp_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {energy}.')
        else:
            gained_energy = energy - temp_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {energy}.')
    elif temp_list[j][0] == 'order':
        if energy >= 30:
            gained_coins = int(temp_list[j][1])
            coins += gained_coins
            energy -= 30
            print(f'You earned {gained_coins} coins.')
        else:
            temp_energy = energy
            energy += 50
            if energy >= 100:
                energy = 100
            print(f'You had to rest!')
    else:
        if coins >= int(temp_list[j][1]):
            print(f'You bought {temp_list[j][0]}.')
            coins -= int(temp_list[j][1])
        else:
            print(f'Closed! Cannot afford {temp_list[j][0]}.')
            is_closed = True
            break

if not is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

