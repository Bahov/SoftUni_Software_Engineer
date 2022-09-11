

length = int(input())
width = int(input())
height = int(input())
perc = float(input())/100

volume_cm = length * width * height #in cm
volume_dm = volume_cm/1000

water_needed = volume_dm * (1 - perc)

print(f'{water_needed}')

