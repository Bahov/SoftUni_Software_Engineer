class Party:
    def __init__(self) -> None:
        self.people = []

command = input()

party = Party()

while command != 'End':
    party.people.append(command)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')