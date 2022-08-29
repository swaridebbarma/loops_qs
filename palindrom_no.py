n=int(input("enter no:-"))
i=n
p=0
while n>0:
    a=n%10
    p=(p*10)+a
    n=n//10
if i==p:
    print("palindrom no:",i)
else:
    print("not palindrom no:",i)
