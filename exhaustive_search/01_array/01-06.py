def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = As[0]
    for Ai in As[1:]:
        if ans < Ai:
            ans = Ai

    # output
    print(ans)


if __name__ == '__main__':
    main()
