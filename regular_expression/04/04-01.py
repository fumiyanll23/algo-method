import re

# input
S = input()

# compute

# output
print(re.sub(r'(?<=r)u(?=r)', 'a', S))
