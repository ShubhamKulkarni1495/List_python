magic = [
    [8,3,4],
    [1,5,9],
    [6,7,2],
] 

row=0
col=0
d1=0
d2=0
i=0
while(i<len(magic)):
    j=0
    while(j<len(magic[i])):
        row=row+magic[i][j]
        col=col+magic[i][j]
        d1=d1+magic[j][j]
        d2=d2+magic[j][-j-1]
        j+=1
    i+=1

print("all row addition",row//len(magic))
print("all column addition",col//len(magic))
print("diagonal 1 addition",d1//len(magic))
print("diagonal 2 addition",d2//len(magic))

if(row==col==d1==d2):
    print("it is a magic square")
else:
    print("it is not a magic square")