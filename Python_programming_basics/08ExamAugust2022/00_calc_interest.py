
base_amount = float(input())
apy = float(input())
compound_period_days = int(input())
hold_period_days = int(input())

interest_per_period = apy / (365 // compound_period_days)

number_of_compoundings = hold_period_days // compound_period_days

result = base_amount * ((1 + interest_per_period) ** number_of_compoundings) - base_amount

print(f"Base amount = {base_amount:.10f}")
print(f"Additional amount after holding {hold_period_days} days at {apy} APY is {result:.10f}")

#0.1157178825

