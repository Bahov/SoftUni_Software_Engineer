number_students = int(input())
number_lectures = int(input())
bonus = int(input())

attendance_list = []
total_bonus_list = []

if number_students == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for student in range(number_students):
        attendance_count = int(input())
        attendance_list.append(attendance_count)
        total_bonus = attendance_count/number_lectures*(5+bonus)
        total_bonus_list.append(total_bonus)

    max_bonus = max(total_bonus_list)
    max_bonus_index = total_bonus_list.index(max_bonus)
    student_attendances = attendance_list[max_bonus_index]

    if max_bonus - int(max_bonus) >=0.5:
        max_bonus += 1

    print(f'Max Bonus: {int(max_bonus)}.')
    print(f'The student has attended {student_attendances} lectures.')