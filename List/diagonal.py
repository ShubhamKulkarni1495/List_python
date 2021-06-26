a=[ [1,2,3],
    [4,5,6],
    [7,8,9]
]
i=0
d1=0
d2=0
while(i<len(a)):
    j=0
    while(j<len(a[i])):
        d1=d1+a[j][j]
        d2=d2+a[j][-j-1]
        j+=1
    i+=1
print("Sum of diagonal one:",d1//3)
print("Sum of diagonal two:",d2//3)