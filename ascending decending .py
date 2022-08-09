# Write a program to sort a dictionary in ascending or descending according to its values .

# dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in dict.values():
#     a=list(dict.items())
#     a.sort()
#     for i in dict.values():
#         b=list(dict.items())
#         b.sort(reverse=True)
# print(a)
# print(b)

d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
p=sorted(d.values())
a={}
for i in p:
    for j in d.keys():
        if d[j]==i:
            a[j]=i
print(a)
