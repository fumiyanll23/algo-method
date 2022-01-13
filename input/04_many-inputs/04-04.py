def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    for A in As:
        if A%3 == 0:
            print(A)


if __name__ == '__main__':
    main()
