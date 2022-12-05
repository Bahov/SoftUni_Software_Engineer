command = input()

dictionary = {}

while command != 'buy':
    command_list = command.split(' ')
    name = command_list[0]
    price = float(command_list[1])
    quantity = int(command_list[2])

    if name not in dictionary.keys():
        dictionary[name] = [quantity, price]
    else:
        dictionary[name][0] += quantity
        dictionary[name].pop(1)
        dictionary[name].append(price)
    
    command = input()

for key,value in dictionary.items():
    print(f'{key} -> {value[0]*value[1]:.2f}')  