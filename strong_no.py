n=int(input("enter no:-"))
tem=n
sum=0
while (n):
    i=1
    fact=1
    rem=n%10
    while i<=rem:
        fact=fact*i
        i+=1
    sum=sum+fact
    n=n//10
if (sum==tem):
    print("strong no:",sum)
else:
    print("not strong no:",sum)