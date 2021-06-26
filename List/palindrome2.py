name=[ 'n', 'a','i','n','a'] 
length=len(name)
reverse=[]
while(length>0):
    reverse+=name[length-1]
    length-=1
if(reverse == name):
    print("it is an palindrome")
else:
    print("it is not an palindrome")