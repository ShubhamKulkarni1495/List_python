#Using for loop
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if(n[i]+n[j]==number):
            print("pair found",[n[i],n[j]])


#Using While loop
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
while(i<len(n)-1):
    j=i+1
    while(j<len(n)):
        if(n[i]+n[j]==number):
            print("pair found",[n[i],n[j]])
        j+=1
    i+=1
    
