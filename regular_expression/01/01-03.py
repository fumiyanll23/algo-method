import re

# input
S = input()

# compute

# output
print('Yes' if re.search(r'^a{1,5}b{10}c*$', S) else 'No')
