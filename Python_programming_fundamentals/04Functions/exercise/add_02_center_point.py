from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def calc_distance(x1,y1,x2,y2):
    return (x2-x1)**2 + (y2-y1)**2

if calc_distance(x1,y1,0,0) <= calc_distance(0,0,x2,y2):
    print(f'({int(floor(x1))}, {int(floor(y1))})')
else:
    print(f'({int(floor(x2))}, {int(floor(y2))})')

