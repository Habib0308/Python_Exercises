"""'
*
* *
* * *
* * * *
* * * * *
"""

n=8
l=[]
mainList=[]
i=1

for a in range(1,n):
    print("a=",a)
    while a>=i:
        print("i=",i)
        l.append("*")
        i+=1
    mainList.append(l)
    l=[]
    i=1
for a in mainList:
    print("".join(a))

""
