count_of_groups = int(input())

group_musala = 0
group_monblan = 0
group_kili = 0
group_k2 = 0
group_everest = 0
all_people = 0

for group in range(count_of_groups):
    people_per_group = int(input())
    all_people += people_per_group
    if people_per_group <= 5:
        group_musala += people_per_group
    elif people_per_group <= 12:
        group_monblan += people_per_group
    elif people_per_group <= 25:
        group_kili += people_per_group
    elif people_per_group <= 40:
        group_k2 += people_per_group
    else:
        group_everest += people_per_group

perc_musala = group_musala / all_people * 100
print(f"{perc_musala:.2f}%")
perc_monblan = group_monblan / all_people * 100
print(f"{perc_monblan:.2f}%")
perc_kili = group_kili / all_people * 100
print(f"{perc_kili:.2f}%")
perc_k2 = group_k2 / all_people * 100
print(f"{perc_k2:.2f}%")
perc_everest = group_everest / all_people * 100
print(f"{perc_everest:.2f}%")