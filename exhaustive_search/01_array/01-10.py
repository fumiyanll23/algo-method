def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ## 1-9の各数字がそれぞれ何回登場するかを数える
    counts = [0] * 9
    for A in As:
        counts[A-1] += 1

    ## 各数字の登場回数の最大値を求める
    target = counts[0]
    ans = 0
    for i, count in enumerate(counts):
        if target < count:
            ans = i + 1
            target = count

    # output
    print(ans)


if __name__ == '__main__':
    main()
