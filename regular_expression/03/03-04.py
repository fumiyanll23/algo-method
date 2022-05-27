import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'^\w+@\w+\.\w{1,4}$', S) else 'No')
