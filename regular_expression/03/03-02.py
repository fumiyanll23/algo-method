import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'\d{3,}', S) else 'No')
