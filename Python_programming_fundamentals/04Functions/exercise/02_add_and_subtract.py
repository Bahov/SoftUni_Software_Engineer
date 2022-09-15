a = int(input())
b = int(input())
c = int(input())

def sum_numbers(a:int, b:int):
    return a + b

def subtract(sum_result, c):
    return sum_result - c

def add_and_subtract(a, b, c):
    sum_result = sum_numbers(a, b)
    print(subtract(sum_result, c))

add_and_subtract(a, b, c)