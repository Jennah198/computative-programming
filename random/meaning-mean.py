t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    cur = a[0]
    for i in range(1, n):
        cur = (cur + a[i]) // 2
    
    print(cur)
