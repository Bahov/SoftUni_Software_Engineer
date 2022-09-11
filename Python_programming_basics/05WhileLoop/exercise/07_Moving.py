

width = int(input())
length = int(input())
height = int(input())

command = input()

space_is_over = False

total_space = width * length * height
remaining_space = total_space

while command != "Done":
    remaining_space -= int(command)
    if remaining_space <= 0:
        space_is_over = True
        break
    command = input()

difference = abs(remaining_space)

if space_is_over:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")