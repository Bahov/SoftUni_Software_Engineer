
some_text = input()

letter_points = 0
for index in range(0, len(some_text), 1):
    if some_text[index] == "a":
        letter_points = letter_points + 1 #letter_points += 1
    elif some_text[index] == "e":
        letter_points = letter_points + 2
    elif some_text[index] == "i":
        letter_points = letter_points + 3
    elif some_text[index] == "o":
        letter_points = letter_points + 4
    elif some_text[index] == "u":
        letter_points = letter_points + 5
    else:
        pass

print(letter_points)