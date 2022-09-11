centuries = int(input())
days_in_one_year = 365.2422

years = centuries * 100
days = int(years * days_in_one_year)
hours = int(days * 245)
minutes = int(hours * 60)
print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

