start_version = list(map(int, input().split('.')))

next_version = start_version

if start_version[2] == 9:
    if start_version[1] == 9:
        next_version[0] += 1
        next_version[1] = 0
        next_version[2] = 0
    else:
        next_version[1] += 1
        next_version[2] = 0
else:
    next_version[2] += 1

print('.'.join(str(x) for x in next_version))