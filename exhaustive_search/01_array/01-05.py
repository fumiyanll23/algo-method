def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    target = As[0]
    for Ai in As[1:]:
        if target < Ai:
            ans += 1
        target = Ai

    # output
    print(ans)


if __name__ == '__main__':
    main()
