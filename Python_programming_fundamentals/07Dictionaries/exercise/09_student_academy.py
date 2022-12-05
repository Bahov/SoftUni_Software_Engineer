lines = int(input())

registry = {}

for _ in range(lines):
    student = input()
    grade = float(input())
    if student in registry.keys():
        registry[student].append(grade)
    else:
        registry[student] = [grade]

for student,grade in registry.items():
    avg_grade = sum(grade)/len(grade)
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")