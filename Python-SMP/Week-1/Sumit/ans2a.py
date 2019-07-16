list=[2,5,6,3,7,5,9,0,2,5]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if(list[i]>list[j]):
            temp=list[i];
            list[i]=list[j]
            list[j]=temp
print(list)
