student_marks=[23,45,89,90,56,80]
length=len(student_marks)
index=0
total=0
while(index<length):
    total=student_marks[index]+total
    print(total)
    index+=1
print("Total Marks are:",total)