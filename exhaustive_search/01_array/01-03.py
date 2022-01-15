def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    print(len([A for A in As if A > 0]))


if __name__ == '__main__':
    main()
