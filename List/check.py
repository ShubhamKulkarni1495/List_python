num=int(input("enter how many inputs you want:"))
i=0
new_list=[]
while(i<num):
    n=int(input("enter the inputs:"))
    new_list.append(n)
    i+=1
print(new_list)

no=int(input("check whether it is present or not:"))
if no in new_list:
    print(no,"is present")
else:
    print(no,"is not present")