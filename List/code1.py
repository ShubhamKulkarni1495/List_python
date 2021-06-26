new_list=[]
i=0
while(i<10):
    num=int(input("enter the numbers:"))
    new_list.append(num)
    i+=1
reversed_list=new_list[::-1]
print("reverse of list",reversed_list)