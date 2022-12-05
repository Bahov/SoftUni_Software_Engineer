data = input()

force_book = {}
user_exists = False
force_exists = False


while data != 'Lumpawaroo':
    if '|' in data:
        data_list = data.split(' | ')
        force_side = data_list[0]
        force_user = data_list[1]
        for value in force_book.values():
            if force_user in value:
                user_exists = True
                break
        if not user_exists:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)
        user_exists = False
    elif '->' in data:
        data_list = data.split(' -> ')
        force_user = data_list[0]
        force_side = data_list[1]
        for key,value in force_book.items():
            if force_user in value:
                user_exists = True
                current_side = key
            if force_side == key:
                force_exists = True
        if not user_exists and not force_exists:
            force_book[force_side] = [force_user]
        elif not user_exists and force_exists:
            force_book[force_side].append(force_user)
        elif user_exists and not force_exists:
            force_book[current_side].remove(force_user)
            force_book[force_side] = [force_user]
        elif user_exists and force_exists:
            force_book[current_side].remove(force_user)
            force_book[force_side].append(force_user)
        user_exists = False
        force_exists = False
        print(f'{force_user} joins the {force_side} side!')
    data = input()

for key,value in force_book.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        print('\n'.join('! ' + user for user in value))
            