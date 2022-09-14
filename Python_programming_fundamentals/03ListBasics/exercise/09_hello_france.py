train_ticket_price = 150
items_collection = input().split('|')
budget_start = float(input())

sell_price = 0
budget = budget_start
sell_price_list = []
profit = 0
final_budget = 0

for item in items_collection:

    items_collection_splt = item.split('->')
    type_item = items_collection_splt[0]
    price_item = float(items_collection_splt[1])

    if (type_item == 'Clothes' and price_item > 50.00) \
        or (type_item == 'Shoes' and price_item > 35.00) \
        or (type_item == 'Accessories' and price_item > 20.50):
        continue

    if price_item > budget:
        continue
    else:
        budget -= price_item
        sell_price = price_item * 1.4
        sell_price_list.append(sell_price)
        profit += price_item * 0.4

final_budget = float(budget + sum(sell_price_list))

for price in range(len(sell_price_list)):
    print(f'{sell_price_list[price]:.2f} ', end = '')

print()

print(f'Profit: {(profit):.2f}')

if final_budget >= train_ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
