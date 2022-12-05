import re

line = input()

pattern = r'((w{3})(\.{1})([a-zA-Z0-9\-]+)(\.[a-z]+)+)'

while line:
    results = re.search(pattern, line)
    if results:
        print(results.group(0))
    line = input()