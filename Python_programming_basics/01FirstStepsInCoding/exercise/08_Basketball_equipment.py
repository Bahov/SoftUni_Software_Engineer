

annual_fee = int(input())

shoes = annual_fee * 0.6
clothes = shoes * 0.8
ball = clothes * 0.25
other = ball * 0.2

total_cost = annual_fee + shoes + clothes + ball + other

print(f'{total_cost:.2f}')