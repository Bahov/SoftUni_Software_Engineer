string_input = input()

my_list = ['Sand', 'Water', 'Fish', 'Sun']
sum_all = 0

string_input = string_input.lower()

for i in my_list:

    sum_all += string_input.count(i.lower())

print(sum_all)