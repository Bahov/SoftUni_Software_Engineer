budget = float(input())
season = input()

destination = ''
percentage = 0.00
resort_type = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        percentage = 0.30
        resort_type = 'Camp'
    else:
        percentage = 0.70
        resort_type = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        percentage = 0.40
        resort_type = 'Camp'
    else:
        percentage = 0.80
        resort_type = 'Hotel'
else:
    destination = 'Europe'
    percentage = 0.90
    resort_type = 'Hotel'

money_spent = budget * percentage
print(f"Somewhere in {destination}")
print(f"{resort_type} - {money_spent:.2f}")
