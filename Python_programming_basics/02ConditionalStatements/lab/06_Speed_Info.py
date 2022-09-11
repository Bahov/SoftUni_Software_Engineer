
user_speed = float(input())

if user_speed <= 10:
    print('slow')
elif user_speed <= 50:
    print('average')
elif user_speed <= 150:
    print('fast')
elif user_speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
