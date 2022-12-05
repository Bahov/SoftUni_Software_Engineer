price_ratings = list(map(int, input().split(', ')))

entry_point = int(input())

item_type = input()

left_list = price_ratings[:entry_point]
right_list = price_ratings[entry_point + 1:]

if item_type == 'cheap':
    left_value = sum(list(filter(lambda x: x < price_ratings[entry_point], left_list )))
    right_value = sum(list(filter(lambda x: x < price_ratings[entry_point], right_list )))
elif item_type == 'expensive':
    left_value = sum(list(filter(lambda x: x >= price_ratings[entry_point], left_list )))
    right_value = sum(list(filter(lambda x: x >= price_ratings[entry_point], right_list )))

if left_value >= right_value:
    print(f'Left - {left_value}')
else:
    print(f'Right - {right_value}')   