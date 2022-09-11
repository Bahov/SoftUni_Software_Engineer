command = input()

is_prime = True
sum_non_prime = 0
sum_prime = 0

while command != 'stop':

    if int(command) < 0:
        print('Number is negative.')
    else:

        for number in range(2, int(command)):
            if int(command) % number == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime += int(command)
        else:
            sum_non_prime += int(command)

    command = input()
    is_prime = True

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
