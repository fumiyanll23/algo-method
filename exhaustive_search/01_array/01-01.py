def main():
    # input
    N, V = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = 'No'
    for A in As:
        if A == V:
            ans = 'Yes'

    # output
    print(ans)


if __name__ == '__main__':
    main()
