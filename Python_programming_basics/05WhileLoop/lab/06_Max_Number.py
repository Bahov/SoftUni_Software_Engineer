import sys

command = input()

max_number = - sys.maxsize
while command != "Stop":
    if max_number < int(command):
        max_number = int(command)
    command = input()

print(f"{max_number}")