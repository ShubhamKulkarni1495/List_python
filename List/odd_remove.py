num = [7,8, 120, 25, 44, 20, 27]
i=0
odd=[]
while(i<len(num)):
	if(num[i]%2!=0):
		odd.append(num[i])
	i+=1
print(odd)