resource = input()
dictionary = {}

while resource != 'stop':
    if resource in dictionary.keys():
        dictionary[resource] += int(input())
    else:
        dictionary[resource] = int(input())

    resource = input()

print('\n'.join(resource + ' -> ' + str(quantity) for resource,quantity in dictionary.items()))


