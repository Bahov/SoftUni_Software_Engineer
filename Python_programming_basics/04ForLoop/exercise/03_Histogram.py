count_of_numbers = int(input())

numbers_group1 = 0
numbers_group2 = 0
numbers_group3 = 0
numbers_group4 = 0
numbers_group5 = 0

for number in range(count_of_numbers):
    manual_input_number = int(input())
    if manual_input_number < 200:
        numbers_group1 += 1
    elif 200 <= manual_input_number <= 399:
        numbers_group2 += 1
    elif 400 <= manual_input_number <= 599:
        numbers_group3 += 1
    elif 600 <= manual_input_number <= 799:
        numbers_group4 += 1
    elif manual_input_number >= 800:
        numbers_group5 += 1

p1 = numbers_group1 / count_of_numbers * 100
p2 = numbers_group2 / count_of_numbers * 100
p3 = numbers_group3 / count_of_numbers * 100
p4 = numbers_group4 / count_of_numbers * 100
p5 = numbers_group5 / count_of_numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
