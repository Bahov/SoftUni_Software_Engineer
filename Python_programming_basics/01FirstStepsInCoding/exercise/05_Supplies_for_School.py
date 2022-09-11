
pen_price = float(5.8)
marker_price = float(7.2)
cleaner_per_litre = float(1.2)

pen_number = int(input())
marker_number = int(input())
cleaner_litre_number = int(input())
discount = int(input())

final_price_no_discount = float(pen_price * pen_number + marker_number * marker_price +
                                cleaner_litre_number * cleaner_per_litre)
discount_amt = float(final_price_no_discount * discount/100)
final_price_with_discount = final_price_no_discount - discount_amt

print(f'{final_price_with_discount:.2f}')

