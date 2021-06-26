#Using for loop
marks =[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]]
sum=0
avg=0
for i in marks:
    for j in i :
        sum+=j
        avg=sum/len(marks)
print(sum)
print(avg)


#Using while loop
marks =[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]]
i=0
sum=0
avg=0
while(i<len(marks)):
    j=0
    while(j<len(marks[i])):
        sum=sum+(marks[i][j])
        avg=sum/len(marks)
        j+=1
    i+=1
print(sum)
print(avg)