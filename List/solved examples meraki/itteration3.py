student_marks=[24,54,39,76,98,75,37,49,43,78]
length=len(student_marks)
index=0
less_than_50=0
greater_than_50=0
while(index<length):
    if(student_marks[index]<50):
        less_than_50=less_than_50+1
    else:
        greater_than_50=greater_than_50+1
    index+=1
print("less than 50 student count:",less_than_50)
print("greater than 50 students count",greater_than_50)   

if(less_than_50+greater_than_50==length):
    print("both are same")
else:
    print("both are different")