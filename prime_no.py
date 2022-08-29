n=int(input("enter no:-"))
i=1
while i<=n:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j+=1
    if c==2:
        print("prime no:",i)
    else:
        print("not prime:",i)
    i+=1


num=int(input('enter your number:-'))
i=1
c=0
while i<=num:
		if num % i ==0:
			c=c+1
		i+=1
if c==2:
		print('prime no:',num)
else:
		print('not prime:',num)
