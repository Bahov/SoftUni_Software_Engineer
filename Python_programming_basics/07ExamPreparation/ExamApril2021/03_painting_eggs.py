egg_size = input()
egg_color = input()
batch_number = int(input())

final_price = 0
if egg_size == "Large":
    if egg_color == "Red":
        final_price = batch_number * 16
    elif egg_color == "Green":
        final_price = batch_number * 12
    elif egg_color == "Yellow":
        final_price = batch_number * 9
elif egg_size == "Medium":
    if egg_color == "Red":
        final_price = batch_number * 13
    elif egg_color == "Green":
        final_price = batch_number * 9
    elif egg_color == "Yellow":
        final_price = batch_number * 7
elif egg_size == "Small":
    if egg_color == "Red":
        final_price = batch_number * 9
    elif egg_color == "Green":
        final_price = batch_number * 8
    elif egg_color == "Yellow":
        final_price = batch_number * 5

final_price_without_cost = final_price * (1 - 0.35)

print(f"{final_price_without_cost:.2f} leva.")