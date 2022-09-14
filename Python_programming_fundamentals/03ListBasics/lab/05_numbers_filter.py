number_of_iterations = int(input())

my_list = []
my_list_filtered = []

for _ in range(number_of_iterations):
    current_number = int(input())
    my_list.append(current_number)

command = input()

# if command == 'even':
#     for i in my_list:
#         if i % 2 == 0 or i == 0:
#             my_list_filtered.append(i)
# elif command == 'odd':
#     for i in my_list:
#         if i % 2 != 0 and i != 0:
#             my_list_filtered.append(i)
# elif command == 'negative':
#     for i in my_list:
#         if i < 0:
#             my_list_filtered.append(i)
# elif command == 'positive':
#     for i in my_list:
#         if i >= 0:
#             my_list_filtered.append(i)

for i in my_list:
    check_condition = (
        (command == 'even' and (i % 2 == 0 or i == 0))
        or (command == 'odd' and i % 2 != 0 and i != 0)
        or (command == 'negative' and i < 0)
        or (command == 'positive' and i >= 0)
    )

    if check_condition:
        my_list_filtered.append(i)

print(my_list_filtered)
