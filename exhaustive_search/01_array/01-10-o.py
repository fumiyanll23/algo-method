from collections import Counter

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    cas = Counter(As)
    print(cas)
    target = cas[As[0]]
    ans = As[0]
    for key, val in cas.items():
        print(key, val, ans, target)
        if target < val:
            ans = key
        target = val

    # output
    print(ans)


if __name__ == '__main__':
    main()
