countries = input().split(', ')
capitals = input().split(', ')

dictionary = dict(zip(countries, capitals))

print('\n'.join(key + ' -> ' + value for key,value in dictionary.items()))