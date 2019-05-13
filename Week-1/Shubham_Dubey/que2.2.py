def binary(a,low,high,key):
    while low<=high:
        mid=int((high+low)/2)
        if a[mid]==key:
            return 1
            break
        elif a[mid]<key:
            low=mid+1
        elif a[mid]>key:
            high=mid-1
    return 0;





a=[1,2,3,4,5,6,7,8,9,10]

no=int(input("Enter the no you want to search"))
if binary(a,0,9,no):
    print("Element found")
else:
    print("Element Not found")
