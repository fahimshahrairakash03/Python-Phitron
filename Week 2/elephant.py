dis = int(input("Distance: "))
s=0
if dis%5 == 0:
    s= int(dis/5)
else:
    s=int(dis/5)+1

print(s)