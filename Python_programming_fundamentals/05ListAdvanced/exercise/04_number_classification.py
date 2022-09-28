input_list = list(map(int, input().split(', ')))

positive_list = [x for x in input_list if x >= 0]
negative_list = [x for x in input_list if x < 0]
even_list = [x for x in input_list if x % 2 == 0]
odd_list = [x for x in input_list if x % 2 != 0]

print(f"Positive: {', '.join(str(x) for x in positive_list)}")
print(f"Negative: {', '.join(str(x) for x in negative_list)}")
print(f"Even: {', '.join(str(x) for x in even_list)}")
print(f"Odd: {', '.join(str(x) for x in odd_list)}")