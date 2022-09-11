key = int(input())
iterations = int(input())

decrypt_char = ''
final_message = ''

for _ in range(iterations):
    char = input()
    decrypt_char = chr(ord(char) + key)
    final_message += decrypt_char

print(final_message)