
choc=int(input("enter chocolate"))
pac = choc
while pac >= 4:
    choc += int(pac/4)
    pac = int(pac/4) + (pac%4)


print(choc)
