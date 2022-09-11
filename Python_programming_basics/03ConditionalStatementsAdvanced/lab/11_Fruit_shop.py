


fruit = str(input())
day_of_week =str(input())
quantity = float(input())

work_days_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekend_days_list = ["Saturday","Sunday"]
fruit_list = ["banana","apple","orange","grapefruit","kiwi","pineapple","grapes"]

price = 0
if day_of_week not in work_days_list and day_of_week not in weekend_days_list:
    print("error")
elif fruit not in fruit_list:
    print("error")
elif day_of_week in work_days_list:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
elif day_of_week in weekend_days_list:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

final_sum = quantity * price

if price == 0:
    pass
else:
    print(f'{final_sum:.2f}')
