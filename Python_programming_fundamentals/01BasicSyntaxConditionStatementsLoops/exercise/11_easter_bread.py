budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 0.75
price_250ml_milk = (price_1kg_flour * 1.25)/4

price_per_bread = price_1kg_flour + price_1pack_eggs + price_250ml_milk

number_breads = int(budget // price_per_bread)

remaining_budget = budget - (number_breads * price_per_bread)

current_eggs_count = 0
current_breads_count = 0

for iteration in range(number_breads):
    current_eggs_count += 3
    current_breads_count += 1
    if current_breads_count % 3 == 0:
        current_eggs_count -= (current_breads_count - 2)

print(f'You made {current_breads_count} loaves of Easter bread! \
Now you have {current_eggs_count} eggs and {remaining_budget:.2f}BGN left.')
