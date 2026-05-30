def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = list(map(int, input().split()))

        possible = True

        for i in range(n):
            if s[i] == 0:
                continue

            left_ok = (i > 0 and s[i-1] < s[i])
            right_ok = (i < n-1 and s[i+1] < s[i])

            if not left_ok and not right_ok:
                possible = False
                break

        if possible:
            print(*s)
        else:
            print(-1)
