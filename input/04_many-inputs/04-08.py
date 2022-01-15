def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]

    # compute

    # output
    print(sum(len(S) for S in Ss))


if __name__ == '__main__':
    main()
