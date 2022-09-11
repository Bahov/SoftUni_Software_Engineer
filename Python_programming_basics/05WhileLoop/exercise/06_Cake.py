

cake_length = int(input())
cake_width = int(input())
command = input()


all_pieces = cake_length * cake_width
pieces_left = all_pieces
cake_is_over = False

while command != "STOP":
    pieces_left -= int(command)
    if pieces_left <= 0:
        cake_is_over = True
        pieces_left = pieces_left * -1
        break
    command = input()

if cake_is_over:
    print(f"No more cake left! You need {pieces_left} pieces more.")
else:
    print(f"{pieces_left} pieces are left.")
