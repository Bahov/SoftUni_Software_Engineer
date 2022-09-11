number_of_stars = int(input())

for i in range(1, number_of_stars + 1):
    print(i * '*')
    if i == number_of_stars:
        for k in range(number_of_stars - 1, 0, -1):
            print(k * '*')

