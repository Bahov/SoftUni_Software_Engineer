input_list = input().split(' ')
count_palindrome = input()

all_palindromes = [x for x in input_list if x == x[::-1]]

print(all_palindromes)
print(f'Found palindrome {all_palindromes.count(count_palindrome)} times')