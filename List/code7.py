even=[]
odd=[]
i=0
while(i<=100):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    i+=1
print(even)
print(odd)