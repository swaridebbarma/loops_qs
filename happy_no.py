n=int(input("enter no;-"))
s=0 
temp=n
while sum!=1 and sum!=4:
    sum=0
    while temp>0:
        a=temp%10
        sum=sum+a**2
        temp=temp//10
    # tem=sum
if sum==1:
    print("happy no:")
else:
    print("not happy no")