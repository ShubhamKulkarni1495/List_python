money=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count1=0
count2=0
while(i<len(money)):
    if(money[i]>10000000):
        count+=1
    elif(money[i]>100000):
        count1+=1
    else:
        count2+=1
    i+=1
print("Number of Crorepatis:",count)
print("Number of Lakhpati:",count1)
print("Number of Dilwale:",count2)