actor_name = input()
academy_points = float(input())
count_of_judges = int(input())

total_points = academy_points
for number in range(1, count_of_judges + 1, 1):
    judge_name = input()
    judge_points = float(input())
    total_points += (len(judge_name) * judge_points) / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
