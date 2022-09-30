input_list = input().split(' ')

# for loop
bakery = {}

for index in range(0, len(input_list), 2):
    bakery[input_list[index]] = int(input_list[index + 1])

print(bakery)

# comprehension

# bakery = {input_list[index] : int(input_list[index + 1]) for index in range(0, len(input_list), 2)}

