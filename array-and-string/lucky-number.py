s = input().strip()
count = 0

for ch in s:
    if ch == '4' or ch == '7':
        count += 1

is_lucky = True
for ch in str(count):
    if ch != '4' and ch != '7':
        is_lucky = False
        break

if is_lucky and count > 0:
    print("YES")
else:
    print("NO")
