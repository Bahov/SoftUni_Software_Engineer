


trip_price = float(input())
puzzles_count = int(input())
doll_count = int(input())
bear_count = int(input())
mini_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
mini_price = 8.20
truck_price = 2.00

total_count = puzzles_count + doll_count + bear_count + mini_count + truck_count 

order_price = puzzles_count * puzzle_price + doll_count * doll_price + bear_count * bear_price + mini_count * mini_price + truck_count * truck_price

final_amount = 0

if total_count >= 50:
    order_price = order_price * 0.75
    final_amount = order_price * 0.90
else:
    final_amount = order_price * 0.90

remaining_money = 0
    
if final_amount >= trip_price:
    remaining_money = final_amount - trip_price
    print(f'Yes! {remaining_money:.2f} lv left.')
else:
    remaining_money = abs(final_amount - trip_price)
    print(f'Not enough money! {remaining_money:.2f} lv needed.')
    

    