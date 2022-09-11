number_of_balls = int(input())

points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
divides_black_balls = 0
for ball in range(1, number_of_balls + 1):
    ball_color = input()
    if ball_color == "red":
        points += 5
        red_balls += 1
    elif ball_color == "orange":
        points += 10
        orange_balls += 1
    elif ball_color == "yellow":
        points += 15
        yellow_balls += 1
    elif ball_color == "white":
        points += 20
        white_balls += 1
    elif ball_color == "black":
        points = points // 2
        divides_black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {divides_black_balls}")