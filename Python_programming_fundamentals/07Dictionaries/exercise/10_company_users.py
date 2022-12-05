command = input()

registry = {}

while command != 'End':
    company = command.split(' -> ')[0]
    employee = command.split(' -> ')[1]

    if company not in registry.keys():
        registry[company] = [employee]
    else:
        if employee not in registry[company]:
            registry[company].append(employee)
    
    command = input()

for company, employee in registry.items():
    print(company)
    print('\n'.join('-- ' + person for person in employee))