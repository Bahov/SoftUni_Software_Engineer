number_of_cities = int(input())

total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    money_earned = float(input())
    expenses = float(input())

    if city % 3 == 0 and city % 5 != 0:
        expenses *= 1.5
    
    if city % 5 == 0:
        money_earned *= 0.9
    
    city_profit = money_earned - expenses
    total_profit += city_profit
    print(f'In {city_name} Burger Bus earned {city_profit:.2f} leva.')

print(f'Burger Bus total profit: {total_profit:.2f} leva.')