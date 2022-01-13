def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    print(A if A%10 < B%10 else B)


if __name__ == '__main__':
    main()
