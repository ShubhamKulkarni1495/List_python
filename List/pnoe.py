num=int(input("enter how many inputs you want:"))
i=0
new_list=[]
positive=[]
negative=[]
odd=[]
even=[]
while(i<num):
    n=int(input("enter the inputs:"))
    new_list.append(n)
    i+=1
print(new_list)
j=0
while(j<len(new_list)):
    if(new_list[j]>0):
        positive.append(new_list[j])
    if(new_list[j]<0):
        negative.append(new_list[j])
    if(new_list[j]%2==0):
        even.append(new_list[j])
    else:
        odd.append(new_list[j])
    j+=1
print("positive number:",positive)
print("negative numbers:",negative)
print("odd numbers:",odd)
print("even numbers:",even)