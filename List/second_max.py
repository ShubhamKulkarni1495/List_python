numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
length=len(numbers)
first_max=numbers[0]
second_max=numbers[0]
while(index<length):
    if(numbers[index]>first_max):
        first_max=numbers[index]
    index+=1

    index2=0
    while(index2<length):
        if(first_max>numbers[index2] and second_max<numbers[index2]):
            second_max=numbers[index2]
        index2+=1
print("second largest is:",second_max)

#using built in methods::
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.sort()
print(numbers[-2])
print()
