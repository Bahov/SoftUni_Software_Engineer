data = input()

dictionary = {}

while not data.isdigit():
    info_list = data.split('-')

    dictionary[info_list[0]] = info_list[1]
    data = input()

iterations = int(data)

for _ in range(iterations):
    data = input()
    if data in dictionary.keys():
        print(f'{data} -> {dictionary[data]}')
    else:
        print(f'Contact {data} does not exist.')