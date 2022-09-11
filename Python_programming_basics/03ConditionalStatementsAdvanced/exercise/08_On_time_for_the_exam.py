exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_hour_minute = exam_hour * 60
arrival_hour_minute = arrival_hour * 60

total_exam_minutes = exam_hour_minute + exam_minute
total_arrival_minutes = arrival_hour_minute + arrival_minute

result = ""
if total_exam_minutes < total_arrival_minutes:
    result = "Late"
elif (total_exam_minutes - 30) <= total_arrival_minutes <= total_exam_minutes:
    result = "On time"
elif total_arrival_minutes < (total_exam_minutes - 30):
    result = "Early"

print(result)

total_minutes_diff = 0
hours_diff = 0
minutes_diff = 0
if total_exam_minutes != total_arrival_minutes:
    if 0 < total_exam_minutes - total_arrival_minutes < 60:
        total_minutes_diff = total_exam_minutes - total_arrival_minutes
        print(f"{total_minutes_diff} minutes before the start")
    elif total_exam_minutes - total_arrival_minutes >= 60:
        total_minutes_diff = total_exam_minutes - total_arrival_minutes
        hours_diff = total_minutes_diff // 60
        minutes_diff = total_minutes_diff % 60
        if minutes_diff < 10:
            print(f"{hours_diff}:0{minutes_diff} hours before the start")
        else:
            print(f"{hours_diff}:{minutes_diff} hours before the start")
    elif total_arrival_minutes - total_exam_minutes < 60:
        total_minutes_diff = abs(total_exam_minutes - total_arrival_minutes)
        print(f"{total_minutes_diff} minutes after the start")
    elif total_arrival_minutes - total_exam_minutes >= 60:
        total_minutes_diff = abs(total_exam_minutes - total_arrival_minutes)
        hours_diff = total_minutes_diff // 60
        minutes_diff = total_minutes_diff % 60
        if minutes_diff < 10:
            print(f"{hours_diff}:0{minutes_diff} hours after the start")
        else:
            print(f"{hours_diff}:{minutes_diff} hours after the start")
else:
    pass



