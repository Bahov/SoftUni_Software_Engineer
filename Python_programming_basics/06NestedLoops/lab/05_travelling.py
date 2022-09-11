destination = input()

saved = 0

while destination != 'End':
    min_budget = float(input())
    saved = 0

    while saved < min_budget:
        saved += float(input())

    print(f'Going to {destination}!')

    destination = input()

