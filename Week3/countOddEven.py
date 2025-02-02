n = int(input("size of array: "))
num = [n]
e =0
o =0
for i in range(n):
    elem = int(input(f"give {i} number: "))
    num.append(elem)

for i in range(n):
    if num[i]%2==0:
        e =e+1
    else:
        o = o+1
print(f"even: {e}, odd: {o}")