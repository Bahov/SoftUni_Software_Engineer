string_input = input()

my_list = string_input.split(' ')
my_list_opp = []

for i in range(len(my_list)):
    my_list_opp.append(int(my_list[i]) * -1)

# print(my_list)
print(my_list_opp)