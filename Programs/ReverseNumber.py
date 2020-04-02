num = input("Enter a number: ")
lenth=len(num)
index=0
sm=0
l=[]
while index < lenth:
    n=num[index]
    l.append(n)
    index+=1
l.reverse()
print("".join(l))

