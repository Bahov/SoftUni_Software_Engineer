number_of_ppl = int(input())
capacity_ppl = int(input())

all_courses = number_of_ppl // capacity_ppl

if number_of_ppl % all_courses != 0:
    all_courses += 1

print(all_courses)