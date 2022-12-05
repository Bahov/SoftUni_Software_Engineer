import re

line = input()

pattern = r'(\=|\/)([A-Z]{1}[a-zA-Z]{2,}\1)'

result = re.findall(pattern, line)

places = []
points = 0
for destination in result:
    place = destination[1].replace('=','')
    place = place.replace('/','')
    places.append(place)
    points += len(place)

print('Destinations: ' + ', '.join(places))
print(f'Travel Points: {points}')