from math import floor

series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_duration = float(input())

episode_duration_with_add = episode_duration * 1.2

total_time = floor(number_of_seasons * number_of_episodes * episode_duration_with_add + number_of_seasons * 10)

print(f"Total time needed to watch the {series_name} series is {total_time} minutes.")