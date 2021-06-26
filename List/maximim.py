numbers = [50, 40, 23, 70, 5, 12, 5, 10, 7]
length=len(numbers)
index=0
minVal=numbers[0]
while(index<length):
    if(minVal>numbers[index]):
        minVal=numbers[index]
    index+=1
print(minVal,"its a minimum")