
print(''.join(list(map(lambda word: word * len(word), input().split(' ')))))

# Option 2
# string_list = input().split(' ')

# result = [word * len(word) for word in string_list]
# print(''.join(result))

# Option 3
# output = ''

# for string in string_list:
#     output += string * len(string)

# print(output)