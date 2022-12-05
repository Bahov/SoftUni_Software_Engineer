text = input()

distinct_chars = set()
message = ''
temp_string = ''

for index in range(len(text)):
    char = text[index]
    if not char.isdigit():
        temp_string += char
        distinct_chars.add(char.lower())
    elif text[index-1].isdigit():
        pass
    else:
        if index != len(text) - 1: # index out of range otherwise
            if not text[index+1].isdigit():
                message += temp_string.upper()*int(char)
            else:
                message += temp_string.upper()*int(char+text[index+1])
        else:
            message += temp_string.upper()*int(char)
        temp_string = ''

print(f'Unique symbols used: {len(distinct_chars)}')
print(message)