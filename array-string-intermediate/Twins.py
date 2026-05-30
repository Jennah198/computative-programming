n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total = sum(coins)
my_sum = 0
count = 0

for c in coins:
    my_sum += c
    count += 1
    if my_sum > total - my_sum:
        break

print(count)
