number = int(input())

is_prime = True

for i in range(2, number, 1):
    if number % i == 0:
        is_prime = False

print(is_prime)
