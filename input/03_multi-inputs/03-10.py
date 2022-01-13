def main():
    # input
    S = input()
    N, M = map(int, input().split())

    # compute

    # output
    print(S[:N-1] + S[M-1] + S[N:M-1] + S[N-1] + S[M:])


if __name__ == '__main__':
    main()
