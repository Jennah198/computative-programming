# Read input
n, m = map(int, input().split())
prices = list(map(int, input().split()))

# Sort prices ascending (most negative first)
prices.sort()

total_savings = 0

# Take up to m items
for i in range(min(m, n)):
    if prices[i] < 0:
        total_savings += -prices[i]  # Add absolute value
    else:
        break  # Stop if price is non-negative

print(total_savings)
