# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}



a={'c1': 'Red', 'c2': 'Green', 'c3': None}
x={}
for k, v in a.items():
   if v!=None:
       x[k]=v

print(x)

