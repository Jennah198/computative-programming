def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        distinct = len(set(a))
        max_color = max(a)

        print(max(distinct, max_color))
