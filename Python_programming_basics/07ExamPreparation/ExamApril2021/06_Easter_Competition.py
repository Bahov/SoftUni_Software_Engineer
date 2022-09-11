number_of_cakes = int(input())

points_person = 0
max_points_person = 0
is_new_leader = False
leader_name = ''
for cake in range(1, number_of_cakes + 1):
    baker_name = input()
    command = input()
    is_new_leader = False
    points_person = 0
    while command != "Stop":
        points_person += int(command)
        command = input()
    if max_points_person < points_person:
        max_points_person = points_person
        leader_name = baker_name
        is_new_leader = True
    else:
        pass
    print(f"{baker_name} has {points_person} points.")
    if is_new_leader:
        print(f"{baker_name} is the new number 1!")
    else:
        pass

print(f"{leader_name} won competition with {max_points_person} points!")

