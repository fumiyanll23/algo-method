def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 1
    for A in As:
        ans *= A

    # output
    print(ans)


if __name__ == '__main__':
    main()
