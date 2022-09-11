
from math import pi

figure_type = str(input())

if figure_type == 'square':
    first_value = float(input())
    square_area = first_value ** 2
    print(f'{square_area:.3f}')
elif figure_type == 'rectangle':
    first_value = float(input())
    second_value = float(input())
    rectangle_area = first_value * second_value
    print(f'{rectangle_area:.3f}')
elif figure_type == 'circle':
    first_value = float(input())
    circle_area = pi * (first_value ** 2)
    print(f'{circle_area:.3f}')
else:
    first_value = float(input())
    second_value = float(input())
    triangle_area = (first_value * second_value)/2
    print(f'{triangle_area:.3f}')