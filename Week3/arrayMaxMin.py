n = 6
num = [n]
m = 0
for i in range(n):
    element = int(input(f"givr {i} number: "))
    num.append(element)
for i in range(n):
    if num[i]>m:
        m=num[i]

print(f"Max: {m}")
