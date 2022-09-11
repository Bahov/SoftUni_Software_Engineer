
total_steps = 0

while total_steps <= 10000:
    steps_walked = input()
    if steps_walked == "Going home":
        steps_going_home = int(input())
        total_steps += steps_going_home
        break
    total_steps += int(steps_walked)

difference = abs(10000 - total_steps)

if total_steps < 10000:
    print(f"{difference} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
