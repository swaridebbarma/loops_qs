n=int(input("enter no:-"))
i=1
s=0
while i<n:
    if (n%i)==0:
        s=s+i
    i+=1
if s==n:
    print('parfect no:',s)
else:
    print("not parfect no:",s)

