command = input()
base_meters = 5364
end_meters = 8848

count_km = base_meters
day_counter = 1
while command != "END":
    meters_climbed = int(input())
    if command == "Yes":
        day_counter += 1
        if day_counter > 5:
            break
        count_km += meters_climbed
    else:
        count_km += meters_climbed
    if count_km >= end_meters or day_counter > 5:
        break
    command = input()

if count_km >= end_meters:
    print(f"Goal reached for {day_counter} days!")
else:
    print("Failed!")
    print(f"{count_km}")


