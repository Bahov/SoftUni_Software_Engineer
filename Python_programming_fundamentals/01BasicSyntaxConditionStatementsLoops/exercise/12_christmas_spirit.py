number_of_decorations = int(input())
days_to_christmas = int(input())

ornament_price = 2
ornament_spirit = 5
skirt_price = 5
skirt_spirit = 3
garland_price = 3
garland_spirit = 10
lights_price = 15
lights_spirit = 17

money_spent = 0
spirit = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        number_of_decorations += 2
    if day % 10 == 0:
        money_spent += skirt_price + garland_price + lights_price
        spirit -= 20
    if day % 2 == 0:
        money_spent += ornament_price * number_of_decorations
        spirit += ornament_spirit
    if day % 3 == 0:
        money_spent += (skirt_price + garland_price) * number_of_decorations
        spirit += skirt_spirit + garland_spirit
    if day % 5 == 0:
        money_spent += lights_price * number_of_decorations
        spirit += lights_spirit
        if day % 3 == 0:
            spirit += 30
    if day == days_to_christmas and day % 10 == 0:
        spirit -= 30

print(f'Total cost: {money_spent}')
print(f'Total spirit: {spirit}')

