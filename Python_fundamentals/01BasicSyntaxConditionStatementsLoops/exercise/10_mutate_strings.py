string_one = input()
string_two = input()
new_string = ''

for letter in range(len(string_one)):
    if string_two[letter] != string_one[letter]:
        new_string = string_two[:letter+1] + string_one[letter+1:]
        print(new_string)


