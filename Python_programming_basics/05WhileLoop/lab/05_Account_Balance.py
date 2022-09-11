
total_sum = 0
while True:
    command = input()
    if command == "NoMoreMoney":
        break
    if float(command) < 0:
        print("Invalid operation!")
        break
    else:
        installment = float(command)
        print(f"Increase: {installment:.2f}")
        total_sum += installment

print(f"Total: {total_sum:.2f}")
