n = int(input("size: "))
num = [n]
m=0
for i in range(n):
    num.append(0)
for i in range(0,n-1):
    elem = int(input("give input: "))
    num[elem] = 1
for i in range(1,n+1):
    # print(num[i])
    if(num[i]==0):
        m= i
print(f"missing number: {m}")
        

