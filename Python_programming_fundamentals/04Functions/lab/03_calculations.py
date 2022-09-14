def calculation(operator, first_int, second_int):
    result = 0
    if operator == 'multiply':
        result = first_int * second_int
    elif operator == 'divide':
        result = first_int / second_int
    elif operator == 'add':
        result = first_int + second_int
    elif operator == 'subtract':
        result = first_int - second_int
    print(int(result))

input1 = input()
input2 = int(input())
input3 = int(input())

calculation(input1, input2, input3)