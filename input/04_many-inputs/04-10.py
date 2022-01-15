def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]

    # compute
    if Ss.count('left') > Ss.count('right'):
        ans = 'left'
    elif Ss.count('left') < Ss.count('right'):
        ans = 'right'
    else:
        ans = 'same'

    # output
    print(ans)


if __name__ == '__main__':
    main()
