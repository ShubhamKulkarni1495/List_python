a = [1,2,3,2,1,3,12,12,32]
i = 0
while i < len(a):
  j = i+1
  while j < len(a):
    if a[i] == a[j]:
      del(a[j])
    j=j+1
  i = i+1
print(a)

#python way
a = [1,2,3,2,1,3,12,12,32]
a = list(set(a))