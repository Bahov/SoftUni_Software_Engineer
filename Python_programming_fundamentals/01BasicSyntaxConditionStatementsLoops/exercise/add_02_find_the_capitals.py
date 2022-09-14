
string = input()

my_list = []

for letter in range(len(string)):
    if string[letter].isupper():
        my_list.append(letter)

print(my_list)