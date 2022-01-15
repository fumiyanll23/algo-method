def main():
    # input
    N, V = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for A in As:
        if A == V:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
