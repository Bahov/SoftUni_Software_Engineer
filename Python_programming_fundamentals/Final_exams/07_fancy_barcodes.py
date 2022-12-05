import re

pattern = r'(\@\#{1,})([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})(\@\#{1,})'
number = int(input())

for _ in range(number):
    line = input()
    result = re.findall(pattern, line)
    if len(result) == 0:
        print('Invalid barcode')
    else:
        product = result[0][1]
        digits_list = [int(x) for x in product if x.isdigit()]
        if len(digits_list) == 0:
            product_group = '00'
        else:
            product_group = ''.join(str(digit) for digit in digits_list)
        print(f'Product group: {product_group}')