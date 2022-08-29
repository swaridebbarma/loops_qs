n=int(input("enter no:-"))
count=0
while n>0:
    a=n%10
    n=n//10
    if a==0:
        count+=1
if count>=1:
    print("duck no:",n)
else:
    print("not duck no",n)