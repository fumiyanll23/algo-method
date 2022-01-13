def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    for A in As:
        print(A % 10)


if __name__ == '__main__':
    main()
