number = int(input())

def perfect_number(number):
    divisor_list = []

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_list.append(divisor)
    
    if sum(divisor_list) == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

perfect_number(number)