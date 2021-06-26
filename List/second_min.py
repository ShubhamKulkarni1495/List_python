numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
length=len(numbers)
first_min=numbers[0]
second_min=numbers[0]
while(index<length):
    if(numbers[index]<first_min):
        first_min=numbers[index]
    index+=1

    index2=0
    while(index2<length):
        if(first_min<numbers[index2] and second_min>numbers[index2]):
            second_min=numbers[index2]
        index2+=1
print("second smallest is:",second_min)

#using built in methods::
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.sort()
print("second smallest:",numbers[1])
print()
