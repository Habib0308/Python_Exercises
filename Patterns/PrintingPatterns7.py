"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
n=5
l=[]
mainList=[]

inside=1
i=1
outside=1
o=9

for a in range(1,n+1):
    while outside<=o:
        l.append(" ")
        outside+=1
    o-=2
    outside=1
    #printed half
    
    while inside<=i:
        l.append("* ")
        inside+=1
    i+=2
    inside=1
    mainList.append(l)
    l=[]
mainList.reverse()
for a in mainList:
    print("".join(a))
