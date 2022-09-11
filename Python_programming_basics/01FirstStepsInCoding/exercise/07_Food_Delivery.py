
chicken = float(10.35)
fish = float(12.40)
vegetarian = float(8.15)

desert_perc = float(0.2)

delivery = float(2.5)

chicken_num = int(input())
fish_num = int(input())
vegetarian_num = int(input())

order_sum = chicken * chicken_num + fish * fish_num + vegetarian * vegetarian_num
desert_sum = order_sum * desert_perc

total_sum = order_sum + desert_sum + delivery

print(f'{total_sum:.2f}')