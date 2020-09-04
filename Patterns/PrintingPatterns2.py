"""
1
12
123
1234
12345
123456
1234567
"""
n=8
l=[]
mainList=[]
i=1


for a in range(1,n):
    while a>=i:
        l.append(str(i))
        int(i)
        i+=1
    mainList.append(l)
    l=[]
    i=1
for a in mainList:
    print("".join(a))
