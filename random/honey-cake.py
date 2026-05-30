import math

w, h, d = map(int, input().split())
n = int(input())

# Get all divisors of n
divs = []
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        divs.append(i)
        if i * i != n:
            divs.append(n // i)

# Try all factorizations
for a in divs:
    if w % a != 0:
        continue
    for b in divs:
        if (n // a) % b != 0:
            continue
        c = n // (a * b)
        if c <= 0:
            continue
        if h % b == 0 and d % c == 0:
            print(a - 1, b - 1, c - 1)
            exit()

print(-1)
