
text_input = input()
vowels_list = ['a','o','u','e','i']
result = [letter for letter in text_input if letter.lower() not in vowels_list]

print(''.join(result))
