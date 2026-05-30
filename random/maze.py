from itertools import permutations

t = int(input())

for _ in range(t):
    n, j, k = input().split()
    j, k = int(j), int(k)

    # Generate and sort permutations
    perms = sorted(''.join(p) for p in permutations(n))

    s1 = perms[j - 1]
    s2 = perms[k - 1]

    # Count A
    A = sum(s1[i] == s2[i] for i in range(len(n)))

    # Count B
    B = len(set(s1) & set(s2)) - A

    print(f"{A}A{B}B")
