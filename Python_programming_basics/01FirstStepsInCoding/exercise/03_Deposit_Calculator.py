
deposit_amt = float(input())
deposit_months = int(input())
deposit_ir = float(input())/100

deposit_result = deposit_amt + deposit_months * ((deposit_amt * deposit_ir)/12)

print(deposit_result)