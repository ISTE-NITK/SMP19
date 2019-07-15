find=[11,12,13,34,56,58,69,34]
position=[]
#finding position of  34
a=34
for i in range(0,len(find)):
    if find[i]==a:
        position.append(i+1)
print(position,sep=',')
print('are the positions of a')
