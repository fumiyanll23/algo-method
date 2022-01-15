def main():
    # input
    N, V = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    if V in As:
        ans = 'Yes'
    else:
        ans = 'No'

    # output
    print(ans)


if __name__ == '__main__':
    main()
