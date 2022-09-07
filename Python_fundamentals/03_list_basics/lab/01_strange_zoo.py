tail_str = input()
body_str = input()
head_str = input()

my_list = [tail_str, body_str, head_str]

my_list.reverse()
# also possible
# my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)