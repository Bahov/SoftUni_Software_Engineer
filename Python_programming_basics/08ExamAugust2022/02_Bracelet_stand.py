available_money_day = float(input())
profit_per_day = float(input())
all_costs = float(input())
present_price = float(input())

money_saved = available_money_day * 5
money_earned = profit_per_day * 5

total_available = money_earned + money_saved - all_costs

difference = abs(total_available - present_price)

if total_available >= present_price:
    print(f"Profit: {total_available:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {difference:.2f} BGN.")