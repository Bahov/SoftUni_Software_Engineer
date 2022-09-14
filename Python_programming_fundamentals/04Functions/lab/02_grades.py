grade_input = float(input())

def grade_word(grade_input):
    if 2.00 <= grade_input <= 2.99:
        print('Fail')
    elif 3.00 <= grade_input <= 3.49:
        print('Poor')
    elif 3.50 <= grade_input <= 4.49:
        print('Good')
    elif 4.50 <= grade_input <= 5.49:
        print('Very Good')
    elif 5.50 <= grade_input <= 6.00:
        print('Excellent')


grade_word(grade_input)