number_of_lines = int(input())

user_and_car = {}

for line in range(number_of_lines):
    command_list = input().split(' ')
    command = command_list[0]
    username = command_list[1]
    if command == 'register':
        license_plate = command_list[2]
        if username in user_and_car.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            user_and_car[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == 'unregister':
        if username not in user_and_car.keys():
            print(f"ERROR: user {username} not found")
        else:
            del user_and_car[username]
            print(f"{username} unregistered successfully")

for username,plate in user_and_car.items():
    print(username + ' => ' + plate)