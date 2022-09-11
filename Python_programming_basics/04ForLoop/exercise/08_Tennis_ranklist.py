
from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

final_points = starting_points
tournaments_won = 0
for tournament in range(number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        final_points += 2000
        tournaments_won += 1
    elif tournament_stage == "F":
        final_points += 1200
    elif tournament_stage == "SF":
        final_points += 720

average_points = floor((final_points - starting_points) / number_of_tournaments)
perc_won_tournaments = tournaments_won / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{perc_won_tournaments:.2f}%")
