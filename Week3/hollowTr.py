n =5
for i in range(n):
    for j in range(i+1):
        if i ==0 or i ==1 or i==n-1 or j==1 or j==i-1:
            print("*",end="")
        else:
            print("",end="")
    print("")     