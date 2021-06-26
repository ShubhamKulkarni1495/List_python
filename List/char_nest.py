char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
c1=1
new_list=[]
while(i<len(char_list)):
    j=0
    while(j<len(char_list)):
        if(char_list[i] == char_list[j]):
            c1+=1
        j+=1
    i+=1
print(c1)