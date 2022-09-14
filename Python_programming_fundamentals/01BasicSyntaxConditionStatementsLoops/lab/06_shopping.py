budget = int(input())
command = input()

is_over_budget = False

while command != 'End':
    budget -= int(command)
    if budget < 0:
        is_over_budget = True
        break
    command = input()

if is_over_budget:
    print('You went in overdraft!')
else:
    print('You bought everything needed.')
