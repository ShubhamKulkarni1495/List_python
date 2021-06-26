numbers=[25, 40, 23, 70, 56, 12, 5, 10, 7] 
index=0
count=0
length=len(numbers)
while(index<length):
    if(numbers[index]>20 and numbers[index]<40):
       count+=1
    index+=1
print("numbers",count)                                                          
