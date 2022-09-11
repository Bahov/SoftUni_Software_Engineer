
dog_food_price = 2.5
cat_food_price = 4

number_of_dog_food = input()
number_of_cat_food = input()

final_amount = float(int(number_of_dog_food) * dog_food_price + int(number_of_cat_food) * cat_food_price)

print(f'{final_amount} lv.')
