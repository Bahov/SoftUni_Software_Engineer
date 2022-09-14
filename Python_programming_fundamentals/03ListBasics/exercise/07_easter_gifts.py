gifts_list = input().split(' ')
command = input()

event = ''
gift = ''

while command != 'No Money':

    command = command.split(' ')
    event = command[0]
    gift = command[1]

    if event == 'OutOfStock':

        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = 'None'

    elif event == 'Required':
        index = int(command[2])

        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif event == 'JustInCase':
        gifts_list[-1] = gift
        
    command = input()

for i in range(len(gifts_list)):
    if gifts_list[i] != 'None':
        print(gifts_list[i] + ' ', end = '')