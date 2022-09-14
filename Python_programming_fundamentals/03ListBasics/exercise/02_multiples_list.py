factor = int(input())
count = int(input())

my_list = []

for i in range(count):
    my_list.append(factor + factor * i)

print(my_list)