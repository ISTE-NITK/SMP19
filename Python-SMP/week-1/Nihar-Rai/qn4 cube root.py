L=[1,15,3,14,13,10,16,17,19,120,26,47,58]
a=[]
for i in L:   a+=( [i] if (i*i*i)%3==1 else [])