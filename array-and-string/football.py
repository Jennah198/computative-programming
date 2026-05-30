t = input()

count = 1  # start with 1 because one character is already a streak

for i in range(1, len(t)):
    if t[i - 1] == t[i]:
        count += 1
    else:
        count = 1  # reset when sequence breaks

    if count == 7:
        print("YES")
        break
else:
    print("NO")
