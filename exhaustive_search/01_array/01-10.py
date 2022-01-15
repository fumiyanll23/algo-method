def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ## 1-9の各数字がそれぞれ何回登場するかを数える
    counts = [0] * 9
    for A in As:
        counts[A-1] += 1
    # print(counts)

    ## 各数字の登場回数の最大値を求める
    target = counts[0]
    ans = 0
    for i, count in enumerate(counts):
        # print(i, target, count, ans)
        if target < count:
            # target = count
            ans = i + 1

    # output
    print(ans)
    # print(target)


if __name__ == '__main__':
    main()
