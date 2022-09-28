to_do_list = [0] * 10

command = input().split('-')

while command[0] != 'End':
    priority = int(command[0]) - 1
    note = command[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority,note)
    command = input().split('-')

result_list = [x for x in to_do_list if x != 0]
print(result_list)