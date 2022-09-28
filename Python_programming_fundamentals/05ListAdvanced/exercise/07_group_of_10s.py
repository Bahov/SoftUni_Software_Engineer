input_list = list(map(int, input().split(', ')))

threshold = 10
current_list = []

while len(input_list) > 0:
    current_list = list(filter(lambda x: x <= threshold, input_list))
    input_list = list(filter(lambda x: x > threshold, input_list))
    print(f"Group of {threshold}'s: {current_list}")
    threshold += 10

