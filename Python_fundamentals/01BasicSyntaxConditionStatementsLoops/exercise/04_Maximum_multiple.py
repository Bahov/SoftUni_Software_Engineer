

divisor = int(input())
boundary = int(input())

found_number = 0

for number in range(1, boundary + 1):
    if number % divisor == 0:
        found_number = number

print(found_number)