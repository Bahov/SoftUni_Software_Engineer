first_number = int(input())
second_number = int(input())

sum_even_position = 0
sum_odd_position = 0

for number in range(first_number, second_number + 1):

    for digit in range(1, 7):

        if digit % 2 == 0:
            sum_even_position += int(str(number)[digit - 1])
        else:
            sum_odd_position += int(str(number)[digit - 1])
    
    if sum_even_position == sum_odd_position:
        print(number, end = ' ')
    
    sum_even_position = 0
    sum_odd_position = 0