a = [3,2,1,4]
n = len(a)
for i in range(n):
    for j in range(i,n):
        if a[i]>a[j] :
            a[i],a[j]= a[j],a[i]
print(a)

