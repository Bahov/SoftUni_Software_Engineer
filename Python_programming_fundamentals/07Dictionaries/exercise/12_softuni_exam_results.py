data = input()

registry = {}
banned_list = []
submissions_dict = {}

while data != 'exam finished':
    data_list = data.split('-')
    if 'banned' not in data:
        username = data_list[0]
        language = data_list[1]
        points = int(data_list[2])
        if language not in submissions_dict.keys():
            submissions_dict[language] = 1
        else:
            submissions_dict[language] += 1
        if username not in registry.keys():
            registry[username] = {language:points}
        elif username in registry.keys() and language not in registry[username].keys():
            registry[username].update({language:points})
        elif username in registry.keys() and language in registry[username].keys():
            if points > registry[username][language]:
                del registry[username][language]
                registry[username].update({language:points})
    else:
        username = data_list[0]
        banned_list.append(username)
    data = input()

print('Results:')
for username, results in registry.items():
    if username not in banned_list:
        for language, points in results.items():
            print(username + ' | ' + str(points))

print('Submissions:')
for key, value in submissions_dict.items():
    print(key + ' - ' + str(value))