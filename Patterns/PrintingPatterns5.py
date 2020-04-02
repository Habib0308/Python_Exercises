"""
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1
"""
n=5
l=[]
mainList=[]
i=1

for a in range(1,n+1):
    while a>=i:
        l.append(str(i))
        int(i)
        i+=1
    mainList.append(l)
    l=[]
    i=1
mainList.reverse()
for a in mainList:
    print("".join(a))
