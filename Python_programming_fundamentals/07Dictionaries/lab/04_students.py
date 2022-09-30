data = input()

students = {}

while ':' in data:
    input_list = data.split(':')
    students[int(input_list[1])] = {input_list[0] : input_list[2]}

    data = input()

course = data.replace('_', ' ')

for key, value in students.items():
    for sub_key,sub_value in value.items():
        if sub_value == course:
            print(f"{sub_key} - {key}")