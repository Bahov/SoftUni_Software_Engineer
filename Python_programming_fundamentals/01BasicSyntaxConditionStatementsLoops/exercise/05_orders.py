
number_of_orders = int(input())

current_order_price = 0
total_order_price = 0

for order in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    
    if (price_capsule < 0.01 or price_capsule > 100.00)  or days not in range(1, 32, 1) or capsules_per_day not in range(1, 2001, 1):
        continue
    else:
        current_order_price = price_capsule * days * capsules_per_day
        print(f'The price for the coffee is: ${current_order_price:.2f}')
        total_order_price += current_order_price

print(f'Total: ${total_order_price:.2f}')
