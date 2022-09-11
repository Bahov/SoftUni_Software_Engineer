

projection = str(input())
rows = int(input())
columns = int(input())

price = 0

if projection == "Premiere":
    price = 12.00
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00

final_result = price * rows * columns

print(f'{final_result:.2f} leva')