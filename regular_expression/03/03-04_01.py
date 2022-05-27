import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]{1,4}$', S) else 'No')
