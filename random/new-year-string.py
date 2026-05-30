def is_good(s):
    return ("2026" in s) or ("2025" not in s)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        if is_good(s):
            print(0)
            continue

        INF = 10**9
        ans = INF

        chars = ['0', '2', '5', '6']

        # brute-force all positions and try fixing minimal characters
        from itertools import product

        for mask in product(chars, repeat=n):
            cost = sum(mask[i] != s[i] for i in range(n))
            if cost >= ans:
                continue
            candidate = ''.join(mask)
            if is_good(candidate):
                ans = cost

        print(ans)
