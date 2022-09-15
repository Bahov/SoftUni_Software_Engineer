data_type = input()
data_input = input()

def data_type_func(data_type, data_input):
    if data_type == 'int':
        return int(data_input) * 2
    elif data_type == 'real':
        return f'{float(data_input) * 1.5:.2f}'
    elif data_type == 'string':
        return f'${data_input}$'

print(data_type_func(data_type, data_input))