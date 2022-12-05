data = input()

total_registry = {}
contest_registry = {}

while data != 'no more time':
    data_list = data.split(' -> ')
    username = data_list[0]
    contest = data_list[1]
    points = int(data_list[2])

    if username not in total_registry.keys():
        total_registry[username] = {contest:points}
    if contest not in total_registry[username].keys():
        total_registry[username][contest] = points
    else:
        if total_registry[username][contest] < points:
            total_registry[username][contest] = points
    
    if contest not in contest_registry.keys():
        contest_registry[contest] = {username:points}
    if username not in contest_registry[contest].keys():
        contest_registry[contest][username] = points
    else:
        if contest_registry[contest][username] < points:
            contest_registry[contest][username] = points
    data = input()

total_user_points = {}

for user, contest in total_registry.items():
    for key,value in contest.items():
        if user not in total_user_points.keys():
            total_user_points[user] = value
        else:
            total_user_points[user] += value

counter = 0

for contest, records in contest_registry.items():
    print(f'{contest}: {len(records)} participants')
    for user, points in dict(sorted(records.items(), key=lambda item: (-item[1], item[0]))).items():
        counter += 1
        print(f'{counter}. {user} <::> {points}')
    counter = 0

print('Individual standings:')
for user, total_points in dict(sorted(total_user_points.items(), key=lambda item: (-item[1], item[0]))).items():
    counter += 1
    print(f'{counter}. {user} -> {total_points}')