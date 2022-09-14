first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')

first_player = False
second_player = False

if first_row.count('1') == 3 \
    or second_row.count('1') == 3 \
    or third_row.count('1') == 3 \
    or (first_row[0] == '1' and second_row[0] == '1' and third_row[0] == '1') \
    or (first_row[1] == '1' and second_row[1] == '1' and third_row[1] == '1') \
    or (first_row[2] == '1' and second_row[2] == '1' and third_row[2] == '1') \
    or (first_row[0] == '1' and second_row[1] == '1' and third_row[2] == '1') \
    or (first_row[2] == '1' and second_row[1] == '1' and third_row[0] == '1'):
    first_player = True
elif first_row.count('2') == 3 \
    or second_row.count('2') == 3 \
    or third_row.count('2') == 3 \
    or (first_row[0] == '2' and second_row[0] == '2' and third_row[0] == '2') \
    or (first_row[1] == '2' and second_row[1] == '2' and third_row[1] == '2') \
    or (first_row[2] == '2' and second_row[2] == '2' and third_row[2] == '2') \
    or (first_row[0] == '2' and second_row[1] == '2' and third_row[2] == '2') \
    or (first_row[2] == '2' and second_row[1] == '2' and third_row[0] == '2'):
    second_player = True

if first_player:
    print('First player won')
elif second_player:
    print('Second player won')
else:
    print('Draw!')