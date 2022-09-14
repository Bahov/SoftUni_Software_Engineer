string_input = input()
numbers_remove = int(input())

my_list = string_input.split(' ')
my_list = list(map(int, my_list))
min_num = 0

for i in range(numbers_remove):
    min_num = min(my_list)
    my_list.remove(min_num)

for i in range(len(my_list)):
    print(str(my_list[i]) + ', ', end = '')