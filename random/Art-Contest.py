g, c, l = map(int, input().split())

scores = [g, c, l]
scores.sort()

if scores[2] - scores[0] >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")
