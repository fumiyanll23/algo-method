import re

# input
N, Y, M = map(int, input().split())
Ss = [input() for _ in range(N)]

# compute
if len(str(M)) == 1:
    M = '0' + str(M)
reg = re.compile(f'\d+_(?=.+)_{Y}{M}\d{2}\.pdf')

# output
print(reg)
for S in Ss:
    print(reg.sub(r'', S))
