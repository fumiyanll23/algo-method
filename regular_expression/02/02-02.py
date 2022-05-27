import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'\(.+\)', S) else 'No')
