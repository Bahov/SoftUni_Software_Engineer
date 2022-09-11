number_of_tabs = int(input())
salary = float(input())

remaining_salary = salary
for tab in range(number_of_tabs):
    tab_name = input()
    if tab_name == "Facebook":
        remaining_salary -= 150
    elif tab_name == "Instagram":
        remaining_salary -= 100
    elif tab_name == "Reddit":
        remaining_salary -= 50
    else:
        pass

    if remaining_salary <= 0:
        print("You have lost your salary.")
        break

if remaining_salary > 0:
    print(f"{remaining_salary:.0f}")
