coffee_stock = input().split(' ')

iterations = int(input())

for iteration in range(iterations):
    command = input()
    if 'Include' in command:
        command_list = command.split(' ')
        coffee_type = command_list[1]
        coffee_stock.append(coffee_type)
    elif 'Remove' in command:
        command_list = command.split(' ')
        number_coffees = int(command_list[2])
        if number_coffees <= len(coffee_stock):
            if 'first' in command:
                count = 0
                for _ in range(number_coffees):
                    del coffee_stock[0]
            elif 'last' in command:
                for _ in range(number_coffees):
                    del coffee_stock[-1]
    elif 'Prefer' in command:
        command_list = command.split(' ')
        first_index = int(command_list[1])
        second_index = int(command_list[2])
        if first_index <= len(coffee_stock) - 1 and second_index <= len(coffee_stock) - 1:
            coffee_stock[first_index], coffee_stock[second_index] = coffee_stock[second_index], coffee_stock[first_index]
    elif 'Reverse' in command:
        coffee_stock.reverse()

print('Coffees:')
print(' '.join(coffee_stock))