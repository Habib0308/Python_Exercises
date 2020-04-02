"""Fibonacci sequence """
l=[0,1]
count=3
num=  input("Enter the number of terms: ")
n=1
for a in l:
    if count<=int(num):
        c=a+l[n]
        l.append(c)
        count+=1
        n+=1
    else:
        break
    
print(l)
