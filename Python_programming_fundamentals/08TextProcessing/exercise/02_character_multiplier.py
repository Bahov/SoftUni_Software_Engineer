line = input().split(' ')

len1 = len(line[0])
len2 = len(line[1])

first = line[0]
second = line[1]
total_sum = 0


for index in range(max(len1,len2)):
    if index > len1-1:
        total_sum += ord(second[index])
    elif index > len2-1:
        total_sum += ord(first[index])
    else:
        temp_sum = ord(first[index]) * ord(second[index])
        # print(temp_sum)
        total_sum += temp_sum

print(total_sum)