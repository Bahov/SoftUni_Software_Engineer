command = input()

cities = {}

while command != 'Sail':
    command_list = command.split('||')
    city = command_list[0]
    population = int(command_list[1])
    gold = int(command_list[2])
    if city in cities.keys():
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    else:
        cities[city] = {'population':population, 'gold':gold}
    command = input()

event = input()

while event != 'End':
    event_list = event.split('=>')
    operation = event_list[0]
    town = event_list[1]
    if operation == 'Plunder':
        people = int(event_list[2])
        gold = int(event_list[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')
    elif operation == 'Prosper':
        gold = int(event_list[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town]['gold'] += gold
            total_gold = cities[town]['gold']
            print(f'{gold} gold added to the city treasury. {town} now has {total_gold} gold.')
    event = input()

if len(cities) == 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city,values in cities.items():
        population = values['population']
        gold = values['gold']
        print(f'{city} -> Population: {population} citizens, Gold: {gold} kg')