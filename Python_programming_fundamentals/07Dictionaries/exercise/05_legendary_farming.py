data = [x.lower() for x in input().split(' ')]

data_add = {'shards':0, 'fragments':0, 'motes':0}

dictionary = {}
dictionary.update(data_add)

goal_reached = False

while True:

    for index in range(0, len(data), 2):
        if data[index+1] in dictionary.keys():
            dictionary[data[index+1]] += int(data[index])
        else:
            dictionary[data[index+1]] = int(data[index])
    
        if dictionary['shards'] >= 250:
            print('Shadowmourne obtained!')
            dictionary['shards'] -= 250
            goal_reached = True
            break
        elif dictionary['fragments'] >= 250:
            print('Valanyr obtained!')
            dictionary['fragments'] -= 250
            goal_reached = True
            break
        elif dictionary['motes'] >= 250:
            print('Dragonwrath obtained!')
            dictionary['motes'] -= 250
            goal_reached = True
            break
    
    if goal_reached:
        break

    data = [x.lower() for x in input().split(' ')]

print('\n'.join(key + ': ' + str(value) for key,value in dictionary.items()))

