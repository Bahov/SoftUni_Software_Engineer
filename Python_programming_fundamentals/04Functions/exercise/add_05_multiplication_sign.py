a = int(input())
b = int(input())
c = int(input())

def multiplication_sign(a,b,c):
    negative_count = 0
    if a < 0:
        negative_count += 1
    if b < 0:
        negative_count += 1
    if c < 0:
        negative_count += 1

    if a == 0 or b == 0 or c == 0:
        return 'zero'
    elif negative_count in (1,3):
        return 'negative'
    elif negative_count in (0,2):
        return 'positive'

print(multiplication_sign(a,b,c))