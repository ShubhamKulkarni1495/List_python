list=[2,3,15,15,3,2]
i=0
mid=(len(list))
same=True
while(i<mid):
    if(list[i] != list[len(list)-i-1]):
        print("No")
        same=False
        break
    i+=1
if(same == True):
    print("Yes")

