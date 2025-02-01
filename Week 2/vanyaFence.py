h = int(input("Hight of fence"))
n = int(input("number of people"))
x=None
w=0
for i in range(n):
    x= int(input("height"))
    if x>h:
        w +=2
    else:
        w = w+1

print(w)