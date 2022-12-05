filepath = input().split('\\')

temp_string=''

for symbol in filepath[-1]:
    if symbol == '.':
        print(f'File name: {temp_string}')
        temp_string = ''
    else:
        temp_string += symbol

print(f'File extension: {temp_string}')