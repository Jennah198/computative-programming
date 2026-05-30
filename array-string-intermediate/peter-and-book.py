n = int(input())
a = list(map(int, input().split()))

day = 0
while n > 0:
    n -= a[day]
    day = (day + 1) % 7

print(day if day != 0 else 7)
