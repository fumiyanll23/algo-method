def main():
    # input
    N, V = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = 1
    for A in reversed(As):
        if A == V:
            print(N - ans)
            return
        else:
            ans += 1

    # output
    print(-1)


if __name__ == '__main__':
    main()
