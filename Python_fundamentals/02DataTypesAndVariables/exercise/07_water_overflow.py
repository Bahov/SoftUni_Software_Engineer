number_of_iterations = int(input())

current_water = 0
remaining_capacity = 255

for iteration in range(number_of_iterations):
    water_inflow = int(input())
    if water_inflow > remaining_capacity:
        print('Insufficient capacity!')
        continue
    else:
        current_water += water_inflow
        remaining_capacity -= water_inflow

print(current_water)



