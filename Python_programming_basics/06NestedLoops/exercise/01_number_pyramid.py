end_number = int(input())

row_counter = 1
printed_numbers = 0

for number in range(1, end_number + 1):

    print(number, end = ' ')
    printed_numbers += 1

    if row_counter == printed_numbers:
        row_counter += 1
        printed_numbers = 0
        print()



