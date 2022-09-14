number_of_snowballs = int(input())

max_weight_sb = 0
max_time_sb = 0
max_value_sb = 0
max_quality_sb = 0

for sb in range(number_of_snowballs):

    weight_sb = int(input())
    time_sb = int(input())
    quality_sb = int(input())

    value_sb = int((weight_sb / time_sb) ** quality_sb)

    if value_sb > max_value_sb:
        max_weight_sb = weight_sb
        max_time_sb = time_sb
        max_value_sb = value_sb
        max_quality_sb = quality_sb

print(f'{max_weight_sb} : {max_time_sb} = {max_value_sb} ({max_quality_sb})')

