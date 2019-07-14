a = [2,4,5,8,9,10]

b = list(x for x in a if (x*x*x)%3==1)

print(b)
