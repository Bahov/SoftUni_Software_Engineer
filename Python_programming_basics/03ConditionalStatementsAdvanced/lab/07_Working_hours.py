

hour = int(input())
day_of_week = str(input())

hour_list = [10,11,12,13,14,15,16,17,18]
day_of_week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

if hour in hour_list and day_of_week in day_of_week_list:
    print("open")
else:
    print("closed")

