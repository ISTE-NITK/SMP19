a = [3,2,1,4]
n = len(a)
for i in range(n):
    for j in range(i,n):
        if a[i]>a[j] :
            a[i],a[j]= a[j],a[i]
print(a)

k = 10
j = 0
for i in a:
    if i == k :
        print("3 is found")
        break
    else :
        j +=1

if j == len(a) :
    print("3 is not found")


