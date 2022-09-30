input_list = input().split(' ')

product_quantity = {input_list[i] : input_list[i+1] for i in range(0, len(input_list), 2)}

search_list = input().split(' ')

for product in search_list:
    if product in product_quantity.keys():
        print(f'We have {product_quantity[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
