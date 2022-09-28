input_int = list(map(int, input().split(', ')))

result_list = [i for i in range(len(input_int)) if input_int[i] % 2 == 0]

print(result_list)