number_input = float(input())

while number_input < 1 or number_input > 100:
    number_input = float(input())

print(f'The number {number_input} is between 1 and 100')