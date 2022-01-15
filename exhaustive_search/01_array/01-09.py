def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    counts = [0] * 9
    for A in As:
        counts[A-1] += 1

    # output
    for count in counts:
        print(count)


if __name__ == '__main__':
    main()
