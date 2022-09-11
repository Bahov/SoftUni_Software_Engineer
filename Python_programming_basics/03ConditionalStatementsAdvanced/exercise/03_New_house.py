
flower_type = str(input())
flower_number = int(input())
budget = int(input())

discount = 0.00
price = 0.00

if flower_type == "Roses":
    price = flower_number * 5
    if flower_number > 80:
        discount = 0.10
    else:
        pass
elif flower_type == "Dahlias":
    price = flower_number * 3.80
    if flower_number > 90:
        discount = 0.15
    else:
        pass
elif flower_type == "Tulips":
    price = flower_number * 2.80
    if flower_number > 80:
        discount = 0.15
    else:
        pass
elif flower_type == "Narcissus":
    price = flower_number * 3
    if flower_number < 120:
        discount = -0.15
    else:
        pass
elif flower_type == "Gladiolus":
    price = flower_number * 2.50
    if flower_number < 80:
        discount = -0.20
    else:
        pass

final_price = price * (1 - discount)

money_left = 0.00
if final_price <= budget:
    money_left = budget - final_price
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {money_left:.2f} leva left.")
else:
    money_left = abs(budget - final_price)
    print(f"Not enough money, you need {money_left:.2f} leva more.")


