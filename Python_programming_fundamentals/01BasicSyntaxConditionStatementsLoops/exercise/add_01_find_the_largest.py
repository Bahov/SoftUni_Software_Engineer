number = int(input())

max_num = ''
num_list = []

for digit in range(len(str(number))):
    num_list.append(int(str(number)[digit]))

for i in range(len(str(number))):
    max_num += str(max(num_list))
    num_list.remove(max(num_list))

print(max_num)