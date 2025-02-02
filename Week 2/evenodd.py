n = int(input("give number: "))
k = int(input("position: "))
number = None
totalOdd = int(n/2)+(n%2)
if k <= totalOdd:
    number = (2*k)-1
else:

    number = (2*(k-totalOdd))

print (int(number))
 