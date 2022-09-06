number_of_courses = int(input())

my_list = []

for i in range(number_of_courses):
    course_name = input()
    my_list.append(course_name)
    # my_list += [course_name]

print(my_list)