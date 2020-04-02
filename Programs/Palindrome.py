num=int(input("Enter a number: "))
n=num
l=[]
while n>0:
    temp=n%10
    n=n//10
    l.append(str(temp))

compare=int("".join(l))

if num==compare:
    print("Palindrome number")
else:
    print("not palindrome number")
