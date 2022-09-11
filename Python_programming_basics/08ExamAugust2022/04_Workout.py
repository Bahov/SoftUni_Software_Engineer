from math import ceil

training_days = int(input())
first_day_km = float(input())

count_days = 0
total_km = first_day_km
new_km = first_day_km
increase = 0
for days in range(1, training_days + 1):
    increase = int(input())
    new_km = new_km * (1 + increase / 100)
    total_km += new_km

diff = ceil(abs(1000 - total_km))
if total_km >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")