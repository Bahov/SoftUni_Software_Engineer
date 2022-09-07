number_of_iterations = int(input())
key_word = input()

my_list = []
my_list_filtered = []

for _ in range(number_of_iterations):
    current_string = input()
    my_list.append(current_string)
    if key_word in current_string:
        my_list_filtered.append(current_string)

print(my_list)
print(my_list_filtered)