n = int(input())
p = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    receiver = p[i]
    ans[receiver - 1] = i + 1

print(*ans)
