control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_per_100m = int(input())

total_seconds_control = control_minutes * 60 + control_seconds

seconds_used = (length / 100) * seconds_per_100m

deduction = (length / 120) * 2.5

total_secs_achieved = seconds_used - deduction

difference = abs(total_seconds_control - total_secs_achieved)
if total_secs_achieved <= total_seconds_control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_secs_achieved:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")

