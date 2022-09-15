def odd_and_even_sum(number:str):
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')

number = input()

odd_and_even_sum(number)
