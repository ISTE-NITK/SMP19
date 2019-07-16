list=[0,1,2,2,3,5,7,8,9,9,9]
p=0
q=len(list)-1
k=3
while(p<=q):
    mid=(p+q)//2
    if(list[mid]==k):
        print("Index:",mid)
        break
    elif(list[mid]<k):
        p=mid+1
    else:
        q=mid-1
if(p>q):
    print("Not found.")
