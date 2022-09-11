limit_fails = int(input())
task_name = input()
grade = int(input())

count_fails = 0
reached_fail_limit = False
count_tasks = 0
sum_grades = 0
last_task = ""
while True:
    count_tasks += 1
    last_task = task_name
    if grade > 4:
        pass
    else:
        count_fails += 1
    if count_fails == limit_fails:
        reached_fail_limit = True
        break
    sum_grades += grade
    task_name = input()
    if task_name == "Enough":
        break
    else:
        grade = int(input())

average_score = sum_grades / count_tasks
if task_name == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_tasks}")
    print(f"Last problem: {last_task}")
if reached_fail_limit:
    print(f"You need a break, {count_fails} poor grades.")
