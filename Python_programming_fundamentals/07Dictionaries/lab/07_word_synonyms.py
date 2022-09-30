iterations = int(input())

dictionary = {}

for _ in range(iterations):
    word, synonym = input(), input()
    if word not in dictionary.keys():
        dictionary[word] = [synonym]
    else:
        dictionary[word].append(synonym)

for key,values in dictionary.items():
    print(f"{key} - {', '.join(values)}")