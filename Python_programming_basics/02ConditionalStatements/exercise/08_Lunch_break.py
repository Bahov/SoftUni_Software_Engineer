
from math import ceil

movie_name = str(input())
movie_time = int(input())
break_time = int(input())

lunch_time = break_time * (1/8)
rest_time = break_time * (1/4)

time_needed = lunch_time + rest_time + movie_time

if time_needed <= break_time:
    time_left = ceil(break_time - time_needed)
    print(f'You have enough time to watch {movie_name} and left with {time_left} minutes free time.')
else:
    time_left = ceil(abs(break_time - time_needed))
    print(f"You don't have enough time to watch {movie_name}, you need {time_left} more minutes.")