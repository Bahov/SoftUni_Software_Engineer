string = input()

while string != 'end':
    print(f'{string} = {string[::-1]}')
    string = input()

# reversed_string = ''

# while string != 'end':
#     for symbol in reversed(string):
#         reversed_string += symbol
#     print(f'{string} = {reversed_string}')
#     reversed_string = ''
#     string = input()