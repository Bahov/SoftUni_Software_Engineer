fire_cells = input().split('#')
water_amount = int(input())

effort = 0
cells_extinguished = []

for fire_cell in fire_cells:

    fire_cell_split = fire_cell.split(' = ')
    type_of_fire = fire_cell_split[0]
    value_of_fire = int(fire_cell_split[1])

    if (type_of_fire == 'High' and value_of_fire not in range(81,125+1) \
        or type_of_fire == 'Medium' and value_of_fire not in range(51,80+1) \
        or type_of_fire == 'Low' and value_of_fire not in range(1,50+1)):
        continue
    
    if water_amount >= value_of_fire:
        water_amount -= value_of_fire
        effort += value_of_fire * 0.25
        cells_extinguished.append(value_of_fire)
    else:
        continue

print('Cells:')
for cell in range(len(cells_extinguished)):
    print(f'- {cells_extinguished[cell]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells_extinguished)}')