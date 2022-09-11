month = input()
nights = int(input())

price_studio = 0
price_apartment = 0
discount_studio = 0.00
discount_apartment = 0.00

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if nights > 14:
        discount_studio = 0.30
    elif nights > 7:
        discount_studio = 0.05
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 14:
        discount_studio = 0.20
    else:
        pass
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if nights > 14:
    discount_apartment = 0.10
else:
    pass

final_price_studio = nights * price_studio * (1 - discount_studio)
final_price_apartment = nights * price_apartment * (1 - discount_apartment)

print(f"Apartment: {final_price_apartment:.2f} lv.")
print(f"Studio: {final_price_studio:.2f} lv.")

