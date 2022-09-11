years_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_received = 0
money_from_toys = 0
for year in range(1, years_lily + 1):
    if year % 2 == 0:
        money_received += (year * 10) / 2 - 1
    else:
        money_from_toys += toy_price

total_money = money_from_toys + money_received

diff = 0
if total_money >= washing_machine_price:
    diff = total_money - washing_machine_price
    print(f"Yes! {diff:.2f}")
else:
    diff = abs(total_money - washing_machine_price)
    print(f"No! {diff:.2f}")
