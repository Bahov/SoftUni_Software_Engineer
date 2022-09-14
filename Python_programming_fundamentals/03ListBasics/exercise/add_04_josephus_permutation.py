orig_list = input().split(' ')
int_list = list(map(int, orig_list))
number_skip = int(input())

counter = 1
index = 0

executed_list = []

while len(executed_list) < len(orig_list):

    if counter % number_skip == 0:
        executed_list.append(int_list[index])
    else:
        int_list.append(int_list[index])

    counter += 1
    index += 1

print(f"[{','.join(str(person) for person in executed_list)}]")




