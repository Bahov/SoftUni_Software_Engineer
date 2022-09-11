budget = int(input())
season = str(input())
fishers_number = int(input())

rent = 0
discount = 0.00
if season == "Spring":
    rent = 3000
    if fishers_number <= 6:
        discount = 0.10
    elif 7 <= fishers_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == "Summer":
    rent = 4200
    if fishers_number <= 6:
        discount = 0.10
    elif 7 <= fishers_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == "Autumn":
    rent = 4200
    if fishers_number <= 6:
        discount = 0.10
    elif 7 <= fishers_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == "Winter":
    rent = 2600
    if fishers_number <= 6:
        discount = 0.10
    elif 7 <= fishers_number <= 11:
        discount = 0.15
    else:
        discount = 0.25

price = rent * (1 - discount)

add_discount = 0.00
if fishers_number % 2 == 0 and season != "Autumn":
    add_discount = 0.05
else:
    pass

final_price = price * (1 - add_discount)

money_left = 0.00
if budget >= final_price:
    money_left = budget - final_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_left = abs(budget - final_price)
    print(f"Not enough money! You need {money_left:.2f} leva.")
