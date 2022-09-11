
import math

first_finish_secs = int(input())
second_finish_secs = int(input())
third_finish_secs = int(input())

total_secs = first_finish_secs + second_finish_secs + third_finish_secs

minutes = math.floor(total_secs/60) # can be done with // целочислено деление, without math.floor
seconds = total_secs % 60

if seconds <= 9:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
    



