

animal = str(input())

mammal_list = ["dog"]
reptile_list = ["crocodile","tortoise","snake"]

if animal in mammal_list:
    print("mammal")
elif animal in reptile_list:
    print("reptile")
else:
    print("unknown")

