num = input("Enter a number: ")
lenth=len(num)
index=0
sm=0

while index < lenth:
    n=int(num[index])
    sm=sm+n
    index+=1

print(sm)

