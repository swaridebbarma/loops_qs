n=int(input("enter no:-"))
i=n
a=0
while n>0:
    a=a+(n%10)*(n%10)*(n%10)
    n=n//10
if i==a:
    print("armstrong no:",i)
else:
    print("not armstrongno:",i)
    