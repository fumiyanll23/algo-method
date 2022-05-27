import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'\d{3}\-\d{4}', S) else 'No')
