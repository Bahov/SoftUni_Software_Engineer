days = int(input())
room_type = input()
evaluation = input()

price_per_night = 0
discount = 0.00

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
    if days < 10:
        discount = 0.30
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
elif room_type == "president apartment":
    price_per_night = 35
    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20

price_after_discount = price_per_night * (days - 1) * (1 - discount)

price_after_eval = 0
if evaluation == "positive":
    price_after_eval = price_after_discount * 1.25
elif evaluation == "negative":
    price_after_eval = price_after_discount * 0.90

print(f"{price_after_eval:.2f}")