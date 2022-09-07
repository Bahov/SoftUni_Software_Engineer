
word = input()

final_string = ''
for letter in range(len(word)-1, -1, -1):
    final_string += word[letter]

print(final_string)

# also possible
# print(word[::-1])

