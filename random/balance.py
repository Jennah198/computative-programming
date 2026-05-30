import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def modinv(x):
    return pow(x, MOD - 2, MOD)

inv2 = modinv(2)

t = int(input())
for _ in range(t):
    q = int(input())

    a = []
    sum_val = 0
    sum_weighted = 0

    for _ in range(q):
        query = input().split()

        if query[0] == '2':
            x = int(query[1])
            L = len(a)

            # update sums
            sum_weighted = (2 * sum_weighted + x * (L + 1) * (L + 2) * inv2) % MOD
            sum_val = (2 * sum_val + x * (L + 1)) % MOD

            # rebuild virtual array
            na = []
            for v in a:
                na.append(x)
                na.append(v)
            na.append(x)
            a = na

        elif query[0] == '1':
            L = len(a)
            mid = (L - 1) // 2
            val = a[mid]

            sum_val = (sum_val - val) % MOD
            sum_weighted = (sum_weighted - val * (mid + 1)) % MOD

            # shift effect
            sum_weighted = (sum_weighted - (sum_val - sum(a[:mid]))) % MOD

            a.pop(mid)

        else:
            L = len(a)
            if L == 1:
                print(a[0] % MOD)
            else:
                print(sum_weighted * pow(2, L - 2, MOD) % MOD)
