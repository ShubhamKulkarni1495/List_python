n= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a=[]
i=0
while (i<len(n)):
	j=i+1
	while (j<len(n)):
		if (n[i]==n[j]):
			a.append(n[i])
		j=j+1
	i=i+1
e=0
b=[ ]
while (e<len(a)):
				if (a[e]) not in b:
					b.append (a[e])
				e=e+1
print(b)