"""
A
B B
C C C
D D D D
E E E E E
"""
n=5
alpha=["0","A","B","C","D","E"]
l=[]
mainList=[]
i=1


for a in range(1,n+1):
    while a>=i:
        l.append(alpha[a])
        i+=1
    mainList.append(l)
    l=[]
    i=1

for a in mainList:
    print("".join(a))

