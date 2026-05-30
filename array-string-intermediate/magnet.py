n = int(input())

prev = input().strip()
groups = 1

for _ in range(1, n):
    curr = input().strip()
    if curr != prev:
        groups += 1
    prev = curr

print(groups)
