# input
X = int(input())
a0, a1, a2, a3 = map(int, input().split())

# compute
As = ((a0, 50), (a1, 10), (a2, 5), (a3, 1))
ans = 0
for A, money in As:
    if X == 0:
        break
    tmp_cnt = X // money
    if tmp_cnt > A:
        X -= A * money
        ans += A
    else:
        X -= tmp_cnt * money
        ans += tmp_cnt

# output
print(ans)
