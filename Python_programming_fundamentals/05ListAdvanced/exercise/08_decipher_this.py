input_list = input().split(' ')

result_list = []

for word in input_list:
    character_code = ''
    string_part = ''
    for letter in range(len(word)):
        if word[letter].isdigit():
            character_code += word[letter]
        else:
            string_part += word[letter]
    first_letter = chr(int(character_code))
    string_list = list(string_part)
    string_list[0], string_list[-1] = string_list[-1], string_list[0]
    string_part = ''.join(string_list)
    result_list.append(first_letter + string_part)

print(' '.join(word for word in result_list))
