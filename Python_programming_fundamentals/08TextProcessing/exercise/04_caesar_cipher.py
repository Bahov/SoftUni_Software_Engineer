line = input()

result = [chr(ord(x)+3) for x in line]

print(''.join(result))
