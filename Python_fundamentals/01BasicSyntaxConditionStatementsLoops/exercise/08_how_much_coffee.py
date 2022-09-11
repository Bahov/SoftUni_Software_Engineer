
command = input()
list_of_events = ['coding','dog','cat','movie','CODING','DOG','CAT','MOVIE']

coffee_counter = 0
is_over_limit = False
while command != 'END':
    if command not in list_of_events:
        pass
    else:
        if command.isupper():
            coffee_counter += 2
        elif command.islower():
            coffee_counter += 1
    if coffee_counter > 5:
        is_over_limit = True
    command = input()

if is_over_limit:
    print('You need extra sleep')
else:
    print(coffee_counter)