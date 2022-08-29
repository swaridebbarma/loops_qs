n=int(input("enter no:-"))
sum=n
temp=n
while sum>9:
    temp=sum
    sum=0
    while temp>0:
        digit= temp%10
        sum+=digit
        temp=temp//10
if sum==1:
    print("magic no:")
else:
    print("not magic no")