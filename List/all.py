elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
sum1=0
count=0
count1=0
while(i<len(elements)):
    if(elements[i]%2==0):
        sum=sum+elements[i]
        count+=1
    else:
        sum1=sum1+elements[i]
        count1+=1
    j=0
    sum2=0
    count2=0
    while(j<len(elements)):
        sum2=sum2+elements[j]
        count2+=1
        j+=1
    i+=1
print("the sum of Even numbers:",sum)
print("count of odd numbers",count)
print("the Average of Even numbers:",sum/count)

print("the sum of Odd numbers:",sum1)
print("count of odd number",count1)
print("the Average of Odd numbers:",sum1/count1)

print("the sum of All numbers:",sum2)
print("count of All number",count2)
print("the Average of Odd numbers:",sum2/count2)
