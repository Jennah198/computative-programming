t = input().strip().lower()

vowels = ['a', 'o', 'y', 'e', 'u', 'i']
result = ""

for i in range(len(t)):
    if t[i] not in vowels:
        result += "." + t[i]

print(result)
