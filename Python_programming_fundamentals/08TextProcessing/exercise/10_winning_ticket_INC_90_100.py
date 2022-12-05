line = [x.strip() for x in input().split(', ')]

distinct_char = set()
win_symbols = ['@', '#', '$', '^' ]
temp_string = ''
right_string = ''
left_string = ''
left_win = False
right_win = False

for ticket in line:
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        for char in ticket:
            distinct_char.add(char)
        if len(distinct_char) == 1:
            print(f"ticket \"{ticket}\" - 10{ticket[0]} Jackpot!")
        else:
            for index in range(10):
                if ticket[index] in win_symbols:
                    if index == 0:
                        temp_string += ticket[index]
                    elif ticket[index-1] == ticket[index]:
                        temp_string += ticket[index]
                        if len(temp_string)>=6:
                            left_win = True
                            left_char = temp_string[0]
                            left_string = temp_string
                    else:
                        temp_string = ''
                        temp_string += ticket[index]
            temp_string = ''
            for index in range(10,20):
                if ticket[index] in win_symbols:
                    if index == 0:
                        temp_string += ticket[index]
                    elif ticket[index-1] == ticket[index]:
                        temp_string += ticket[index]
                        if len(temp_string)>=6:
                            right_win = True
                            right_char = temp_string[0]
                            right_string = temp_string
                    else:
                        temp_string = ''
                        temp_string += ticket[index]
            temp_string = ''
            if left_win and right_win and left_char==right_char:
                print(f"ticket \"{ticket}\" - {min(len(left_string),len(right_string))}{left_string[0]}")
            else:
                print(f"ticket \"{ticket}\" - no match")
            temp_string = ''
            left_win = False
            right_win = False
            left_char = ''
            right_char = ''