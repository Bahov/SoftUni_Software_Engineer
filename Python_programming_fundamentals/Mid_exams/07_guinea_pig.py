food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())

day_counter = 1
while day_counter <= 30:
    food_kg -= 0.3
    if day_counter % 2 == 0:
        hay_kg -= 0.05 * food_kg
    if day_counter % 3 == 0:
        cover_kg -= (1/3) * weight_kg
    
    if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
        print('Merry must go to the pet store!')
        break
    day_counter += 1

if food_kg > 0 and hay_kg > 0 and cover_kg > 0:
    print(f'Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.')
