
nylon_per_sqm = float(1.5)
paint_per_ltr = float(14.5)
razreditel_per_ltr = float(5.0)
add_paint_perc = float(0.1)
add_nylon_sqm = float(2.0)
bags = float(0.4)
price_per_hour_perc = float(0.3)

req_nylon_sqm = int(input())
req_paint_ltr = int(input())
req_razr_ltr = int(input())
req_hours = int(input())

sum_all_material = (req_nylon_sqm + 2) * nylon_per_sqm + req_paint_ltr * (1+add_paint_perc) * paint_per_ltr \
                   + req_razr_ltr * razreditel_per_ltr + bags

work_price = sum_all_material * price_per_hour_perc * req_hours

total_price = sum_all_material + work_price

print(f'{total_price:.2f}')