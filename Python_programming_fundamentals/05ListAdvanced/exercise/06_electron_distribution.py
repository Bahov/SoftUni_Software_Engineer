number_of_electrons = int(input())

def fill_shells(number_of_electrons):
    remaining_electrons = number_of_electrons
    current_shell = 1
    filled_shells = []
    while True:
        if remaining_electrons >= 2 * current_shell ** 2:
            filled_shells.append(2 * current_shell ** 2)
            remaining_electrons -= 2 * current_shell ** 2
            current_shell += 1
        else:
            filled_shells.append(remaining_electrons)
            break
    return filled_shells

print(fill_shells(number_of_electrons))