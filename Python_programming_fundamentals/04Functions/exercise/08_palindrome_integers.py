
number_list = input().split(', ')

for number in number_list:
    if number == number[::-1]:
        print('True')
    else:
        print('False')

