contest_data = input()

contest_pass = {}

while contest_data != 'end of contests':
    contest_data_list = contest_data.split(':')
    contest = contest_data_list[0]
    password = contest_data_list[1]
    contest_pass[contest] = password
    contest_data = input()

submission_data = input()
submissions = {}

while submission_data != 'end of submissions':
    submission_data_list = submission_data.split('=>')
    contest = submission_data_list[0]
    password = submission_data_list[1]
    username = submission_data_list[2]
    points = int(submission_data_list[3])

    if contest in contest_pass.keys() and password == contest_pass[contest]:
        if username in submissions.keys() and contest in submissions[username].keys():
            if submissions[username][contest] < points:
                submissions[username][contest] = points
        else:
            if username in submissions.keys():
                submissions[username].update({contest:points})
            else:
                submissions[username] = {contest:points}
    submission_data = input()

total_points = 0
max_user = ''
max_points = 0

for username, sub_dict in submissions.items():
    for contest, points in sub_dict.items():
        total_points += points
    if max_user == '':
        max_user = username
        max_points = total_points
    elif total_points > max_points:
        max_user = username
        max_points = total_points
    total_points = 0

print(f'Best candidate is {max_user} with total {max_points} points.')

sorted_submissions = dict(sorted(submissions.items()))

print('Ranking:')
for username, sub_dict in sorted_submissions.items():
    print(username)
    for contest, points in dict(sorted(sub_dict.items(), key=lambda item: item[1], reverse= True)).items():
        print(f'#  {contest} -> {points}')