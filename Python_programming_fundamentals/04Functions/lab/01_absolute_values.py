input_string = input().split(' ')

result = []

for number in input_string:
    result.append(abs(float(number)))

print(result)

# # map() and list comprehension

# input_numbers = list(map(float, input().split(' ')))
# result = [abs(number) for number in input_numbers]
# print(result)

# # function

# def abs_float(input_list):
#     result = [abs(float(num)) for num in input_list]
#     return result

# string_list = input().split(' ')

# print(abs_float(string_list))
