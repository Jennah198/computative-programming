t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    q.sort()
    r.sort()

    i = j = 0
    ans = 0

    while i < n and j < n:
        if q[i] * (r[j] + 1) + r[j] <= k:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1

    print(ans)
