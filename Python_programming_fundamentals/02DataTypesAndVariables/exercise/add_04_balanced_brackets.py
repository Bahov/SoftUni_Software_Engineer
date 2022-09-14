iterations = int(input())

open_bracket_count = 0
close_bracket_count = 0
stop_flag = False

submitted_brackets = []

for _ in range(0, iterations):
    string_input = input()

    if string_input not in ['(',')']:
        continue

    if len(submitted_brackets) == 0 and string_input == ')':
        stop_flag = True
        break
    
    if len(submitted_brackets) == 0:
        submitted_brackets.append(string_input)
    else:
        if string_input == submitted_brackets[-1]:
            stop_flag = True
            break
        else:
            submitted_brackets.append(string_input)

if stop_flag:
    print('UNBALANCED')
else:
    print('BALANCED')

