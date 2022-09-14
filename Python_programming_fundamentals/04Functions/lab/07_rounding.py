print(list(map(lambda x: round(float(x)), input().split(' '))))

# # Option 2
# input_numbers = list(map(float, input().split(' ')))

# def round_func(input_numbers: list):
#     int_list = []
#     for number in input_numbers:
#         int_list.append(round(number))
#     return int_list

# print(round_func(input_numbers))