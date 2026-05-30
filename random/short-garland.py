import sys
input = sys.stdin.readline
MOD = 998244353

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    parents = list(map(int, input().split()))

    # Build depth array
    depth = [0] * n
    for i in range(1, n):
        depth[i] = depth[parents[i-1] - 1] + 1

    # Count nodes per depth
    from collections import Counter
    cnt = Counter(depth)

    max_depth = max(cnt)
    ways = 1

    # Sliding window sum of available parents
    window_sum = 1  # depth 0 (root)

    for d in range(1, max_depth + 1):
        # Remove nodes too far
        if d - k - 1 >= 0:
            window_sum -= cnt[d - k - 1]

        if window_sum <= 0:
            ways = 0
            break

        ways = ways * pow(window_sum, cnt[d], MOD) % MOD
        window_sum += cnt[d]

    print(ways)
