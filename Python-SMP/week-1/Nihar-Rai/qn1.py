list1 = ['I','S','T','E']
list2 = list1 #list2 points at same object as 1
list2[0] ='1'#change in 0 position changes list1 too since same object is being used by both lists
print(list1)
list1 = list1 + []
list2[1] = 2
print(list1)#not sure why there is no change
list1 = ['I','S','T','E']
list2 = list1# same as above
list2[0] = '1'
print(list1)
list1+=[]# blank space is added to left of list1
list2[1] = 2
print(list1)#object list1 and 2 point to are still same so all changes in list2 are observed