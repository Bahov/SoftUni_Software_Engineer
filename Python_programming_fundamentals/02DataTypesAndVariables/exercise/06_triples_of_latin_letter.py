number_of_letters = int(input())

for i in range(number_of_letters):
    for k in range(number_of_letters):
        for j in range(number_of_letters):
            print(chr(97 + i) + chr(97 + k) + chr(97 + j))