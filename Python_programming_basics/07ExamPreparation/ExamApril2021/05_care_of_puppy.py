food_bought_kg = int(input())
command = input()
food_bought_gram = food_bought_kg * 1000

remaining_food = food_bought_gram
while command != "Adopted":
    remaining_food -= int(command)
    command = input()

if remaining_food >= 0:
    print(f"Food is enough! Leftovers: {remaining_food} grams.")
else:
    print(f"Food is not enough. You need {remaining_food * (-1)} grams more.")
