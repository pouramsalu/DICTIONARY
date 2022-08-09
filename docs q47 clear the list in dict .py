# # A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary. 
# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for k in a.keys():
#     a[k]=[]
# print(a)


# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# x=[]
# for i,j in a.items():
#     if len(j)>0:
#         b=i,[]
#         x.append(b)
# print(x)

a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
x=[]
for i,j in a.items():
    if len(j)>0:
        b=i,[]
        x.append(b)
print(x)

