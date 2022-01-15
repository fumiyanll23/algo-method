def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    maxi = As[0]
    ans = 0
    for i, Ai in enumerate(As[1:]):
        if maxi < Ai:
            maxi = Ai
            ans = i + 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
