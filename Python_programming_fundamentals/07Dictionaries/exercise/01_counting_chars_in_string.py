text = input().replace(' ','')

result = {}

for index,char in enumerate(text):
    if char in result.keys():
        result[char] += 1
    else:
        result[char] = 1

print('\n'.join(key + ' -> ' + str(value) for key,value in result.items()))