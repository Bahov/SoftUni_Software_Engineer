num_iterations = int(input())

for _ in range(num_iterations):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')