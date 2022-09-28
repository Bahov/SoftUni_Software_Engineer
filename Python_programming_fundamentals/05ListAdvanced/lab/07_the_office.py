from statistics import mean

happiness_list = list(map(int, input().split(' ')))
factor = int(input())

happiness_map = list(map(lambda x: x * factor, happiness_list))

average_happiness = mean(happiness_map)

happiness_filtered = list(filter(lambda x: x >= average_happiness, happiness_map))

if len(happiness_filtered) >= len(happiness_list) / 2:
    print(f'Score: {len(happiness_filtered)}/{len(happiness_list)}. Employees are happy!')
else:
    print(f'Score: {len(happiness_filtered)}/{len(happiness_list)}. Employees are not happy!')