number_list = input().split(' ')
string = input()

message = ''

for number in number_list:
    sum = 0
    
    for digit in number:
        sum += int(digit)

    sum %= len(string)
            
    message += string[sum]
    string = string[:sum] + string[sum + 1:]    

print(message)