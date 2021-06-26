char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
while(i<len(char_list)):
    if(char_list[i] == "a"):
        c1+=1
    elif(char_list[i] == "n"):
        c2+=1
    elif(char_list[i] == "t"):
        c3+=1
    elif(char_list[i] == "x"):
        c4+=1
    elif(char_list[i] == "u"):
        c5+=1
    else:
        c6+=1
    i+=1
print(c1,"Number of a")
print(c2,"Number of n")
print(c3,"Number of t")
print(c4,"Number of x")
print(c5,"Number of u")
print(c6,"Number of g")