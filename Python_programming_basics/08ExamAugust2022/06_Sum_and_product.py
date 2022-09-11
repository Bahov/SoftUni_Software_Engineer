division_number = int(input())
last_digit = len(str(division_number)) - 1
is_found = False

for a in range(1 , 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, -1):
                if (a + b + c + d) == (a * b * c * d) and str(division_number)[last_digit] == '5':
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and division_number % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_found = True
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

if is_found is False:
    print("Nothing found")
