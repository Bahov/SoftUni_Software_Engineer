import re

line = input()

pattern = r'>{2}([a-zA-Z]+)<{2}(\d+\.?\d+)\!{1}(\d+)' 
# results = re.findall(pattern, line)
# print(results)

furniture_list = []
total_cost = 0
while line != 'Purchase':
    results = re.findall(pattern, line)
    if len(results) > 0:
        furniture_list.append(results[0][0])
        total_cost += float(results[0][1]) * int(results[0][2])
    line = input()

print('Bought furniture:')
for item in furniture_list: print(item)
print(f'Total money spend: {total_cost:.2f}')