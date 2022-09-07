number_of_iterations = int(input())

positive = []
negative = []
sum_negative = 0

for i in range(number_of_iterations):
    current_int = int(input())
    if current_int >= 0:
        positive.append(current_int)
    else:
        negative.append(current_int)

for i in negative:
    sum_negative += i

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum_negative}')

