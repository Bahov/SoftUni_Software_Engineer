names = input().split(', ')

result = sorted(names, key = lambda element: (-len(element), element))

print(result)