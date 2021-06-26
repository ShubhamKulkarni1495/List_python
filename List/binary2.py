num=[1, 0, 0, "1", 1]
a=0
i=-1
sum=0
while i>=(-len(num)):
	if(num[i]<=1):
	    sum=sum+(num[i]*2**a)
	    a=a+1
	else:
	    print("binary numbers are not in 0 and 1")
	    break
	i=i-1
print(sum)