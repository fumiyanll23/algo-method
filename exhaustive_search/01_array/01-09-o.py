from collections import Counter

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    for i in range(1, 10):
        print(Counter(As)[i])


if __name__ == '__main__':
    main()
