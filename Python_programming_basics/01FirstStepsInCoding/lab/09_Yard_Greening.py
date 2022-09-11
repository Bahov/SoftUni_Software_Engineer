
sqm = float(input())

discount_amt = float(sqm * 7.61 * 0.18)

final_price = float(sqm * 7.61 - discount_amt)

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_amt} lv.')


