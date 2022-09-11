


current_record_secs = float(input())
distance_meters = float(input())
secs_per_meter = float(input())

resistance = 12.5

delay_times = distance_meters // 15

achieve_secs_no_delay = distance_meters * secs_per_meter
achieve_secs_with_delay = achieve_secs_no_delay + delay_times * resistance

if achieve_secs_with_delay < current_record_secs:
    print(f'Yes, he succeeded! The new world record is {achieve_secs_with_delay:.2f} seconds.')
else:
    secs_less = abs(achieve_secs_with_delay - current_record_secs)
    print(f'No, he failed! He was {secs_less:.2f} seconds slower.')



