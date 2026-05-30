s = int(input())
stewards = list(map(int, input().split()))

mn = min(stewards)
mx = max(stewards)

count = 0
for x in stewards:
    if mn < x < mx:
        count += 1

print(count)
