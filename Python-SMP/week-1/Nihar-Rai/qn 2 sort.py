sort=[1,2,3,6,3,7,5,8,2]
for i in range(0,len(sort)):
    for j in range(0,len(sort)):
        if sort[i]<sort[j]:
            sort[i]=sort[i]+sort[j]
            sort[j]=sort[i]-sort[j]
            sort[i]=sort[i]-sort[j]
print(sort)