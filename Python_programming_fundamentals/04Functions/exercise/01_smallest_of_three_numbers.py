
numbers_list =[]

for number in range(3):
    numbers_list.append(int(input()))

def min_of_three_numbers(numbers_list: list):
    return min(numbers_list)

print(min_of_three_numbers(numbers_list))


# # Option 2
# a = int(input())
# b = int(input())
# c = int(input())

# def min_of_three_numbers(a: int, b: int, c: int):
#     return min(a,b,c)

# print(min_of_three_numbers(a,b,c))

