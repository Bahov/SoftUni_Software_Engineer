

result = list(filter(lambda x: x % 2 == 0, [int(i) for i in input().split(' ')]))
print(result)

# # Option 2
# result = list(filter(lambda x: int(x) % 2 == 0, input().split(' ')))
# result = list(map(int, result))

# print(result)
