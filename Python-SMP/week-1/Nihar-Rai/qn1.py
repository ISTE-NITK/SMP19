list1 = ['I','S','T','E']
list2 = list1 #list2 points at same object as 1
list2[0] ='1'#change in 0 position changes list1 too since same object is being used by both lists
print(list1)
list1 = list1 + []#item is added 
list2[1] = 2
print(list1)
#Output1 ['1','S','T','E']
#output2 ['1','S','T','E']
list1 = ['I','S','T','E']
list2 = list1# same as above
list2[0] = '1'
print(list1)
list1+=[]# blank space is added to left of list1
list2[1] = 2
print(list1)#object list1 and 2 point to, are still same so all changes in list2are observed
#output1 ['1','S','T','E']
#output2 ['1',2,'T','E']
