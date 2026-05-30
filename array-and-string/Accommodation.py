r = int(input())

count = 0

for i in range(r):
    p, q = map(int, input().split())
    if q - p >= 2:
       count +=1

print(count)