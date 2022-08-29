n=int(input("enter no:-"))
i=n
s=0
while i>0:
    s=(i%10)+s
    i=i//10
if n%s==0:
    print("harshad no:",n)
else:
    print("not harshad no:",n)