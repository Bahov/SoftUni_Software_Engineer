string_input = input()

my_list = string_input.split(', ')

my_list.reverse()

if my_list[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    sheep_number = my_list.index('wolf')
    print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
