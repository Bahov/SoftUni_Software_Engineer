count_numbers = int(input())

def tribonacci_seq(count_numbers):
    my_list = []
    num = 0
    for i in range(count_numbers):
        if i in (0,1):
            print('1', end = ' ')
            my_list.append(1)
        elif i == 2:
            num = sum(my_list)
            print(num, end = ' ')
            my_list.append(num)
        else:
            num = my_list[i-3] + my_list[i-2] + my_list[i-1]
            print(num, end = ' ')
            my_list.append(num)

tribonacci_seq(count_numbers)