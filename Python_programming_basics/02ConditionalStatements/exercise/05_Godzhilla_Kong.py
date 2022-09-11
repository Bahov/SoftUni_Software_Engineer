


budget = float(input())
stat_count = int(input())
clothes_price = float(input())

decor = budget * 0.1

clothes_total_price = stat_count * clothes_price

if stat_count > 150:
    clothes_total_price = clothes_total_price * 0.9
    
total_amount = decor + clothes_total_price


if total_amount > budget:
    remaining_money = abs(budget - total_amount)
    print(f'Not enough money!')
    print(f'Wingard needs {remaining_money:.2f} leva more.')
else:
    remaining_money = budget - total_amount
    print(f'Action!')
    print(f'Wingard starts filming with {remaining_money:.2f} leva left.')
    
    