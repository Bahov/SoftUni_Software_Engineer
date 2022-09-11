


budget = float(input())
videocard_count = int(input())
cpu_count = int(input())
ram_count = int(input())

videocard_price = 250
videocard_amount = videocard_count * videocard_price
cpu_price = videocard_amount * 0.35
ram_price = videocard_amount * 0.10

total_amount = videocard_count * videocard_price + cpu_count * cpu_price + ram_count * ram_price

final_amount = 0
if videocard_count > cpu_count:
    final_amount = total_amount * 0.85
    
else:
    final_amount = total_amount
    
remaining_budget = 0
if budget >= final_amount:
    remaining_budget = budget - final_amount 
    print(f'You have {remaining_budget:.2f} leva left!')
else:
    remaining_budget = abs(budget - final_amount)
    print(f'Not enough money! You need {remaining_budget:.2f} leva more!')


