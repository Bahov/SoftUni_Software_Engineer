


hour = int(input())
minutes = int(input())

total_minutes = (hour * 60) + minutes + 15

hours_final = total_minutes // 60
minutes_final = total_minutes % 60

if hours_final > 23:
    hours_final = hours_final - 24
else:
    pass

if minutes_final < 10:
    print(f'{hours_final}:0{minutes_final}')
else:
    print(f'{hours_final}:{minutes_final}')