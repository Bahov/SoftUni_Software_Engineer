change = float(input())
change = int(change * 100)

total_coins = 0

while change > 0:
    if change - 200 >= 0:
        total_coins += 1
        change -= 200
    elif change - 100 >= 0:
        total_coins += 1
        change -= 100
    elif change - 50 >= 0:
        total_coins += 1
        change -= 50
    elif change - 20 >= 0:
        total_coins += 1
        change -= 20
    elif change - 10 >= 0:
        total_coins += 1
        change -= 10
    elif change - 5 >= 0:
        total_coins += 1
        change -= 5
    elif change - 2 >= 0:
        total_coins += 1
        change -= 2
    else:
        total_coins += 1
        change -= 1


print(f"{total_coins}")
