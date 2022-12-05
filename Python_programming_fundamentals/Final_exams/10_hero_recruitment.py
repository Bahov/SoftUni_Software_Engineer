
hero_dict = {}

command = input()

while command != 'End':
    command_list = command.split(' ')
    action = command_list[0]
    hero_name = command_list[1]
    if action == 'Enroll':
        if hero_name in hero_dict.keys():
            print(f'{hero_name} is already enrolled.')
        else:
            hero_dict.update({hero_name:[]})
    if action == 'Learn':
        spell_name = command_list[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in hero_dict[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}")
        else:
            hero_dict[hero_name].append(spell_name)
    if action == 'Unlearn':
        spell_name = command_list[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in hero_dict[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}")
        else:
            hero_dict[hero_name].remove(spell_name)
    command = input()

print('Heroes:')
for hero, spells in hero_dict.items():
    print(f"== {hero}: {', '.join(spells)}")