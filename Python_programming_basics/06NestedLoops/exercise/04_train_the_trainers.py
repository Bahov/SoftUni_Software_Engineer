people_jury = int(input())
presentation = input()

sum_evaluation = 0
average_grade = 0
sum_average_grade = 0
number_of_presentations = 0
while presentation != "Finish":
    sum_evaluation = 0
    for grade in range(1, people_jury + 1):
        evaluation = float(input())
        sum_evaluation += evaluation
    average_grade = sum_evaluation / people_jury
    print(f"{presentation} - {average_grade:.2f}.")
    sum_average_grade += average_grade
    number_of_presentations += 1
    presentation = input()

total_average_grade = sum_average_grade / number_of_presentations
print(f"Student's final assessment is {total_average_grade:.2f}.")




