product = input()
quantity = int(input())

def total_order_price(product: str, quantity: int):
    price = 0
    if product == 'coffee':
        price = 1.5
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.4
    elif product == 'snacks':
        price = 2
    
    return f'{quantity * price:.2f}'

print(total_order_price(product, quantity))