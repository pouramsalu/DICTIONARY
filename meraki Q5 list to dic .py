# create a dictionary from 2 lists,where the elements of 1st list are the keys
# and the elemnets of the 2nd list are the corresponding values

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
l={}
i=0
while i<len(list1):
    l[list1[i]]=list2[i]
    i+=1
print(l)