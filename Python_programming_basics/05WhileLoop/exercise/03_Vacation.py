vacation_cost = float(input())
available_money = float(input())

spend_counter = 0
days_passed = 0
while True:
    action = input()
    money_used = float(input())
    days_passed += 1
    if action == "spend":
        spend_counter += 1
        available_money -= money_used
        if spend_counter == 5:
            print("You can't save the money.")
            print(f"{days_passed}")
            break
        elif available_money < 0:
            available_money = 0
    if action == "save":
        spend_counter = 0
        available_money += money_used
        if available_money >= vacation_cost:
            print(f"You saved the money for {days_passed} days.")
            break
