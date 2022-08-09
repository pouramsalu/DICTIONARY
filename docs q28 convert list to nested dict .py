# Write a Python program to convert a list into a nested dictionary of keys.
dict= [1, 2, 3, 4]
a={}
b={}
for i in dict[: :-1]:
    a[i]=b
    b=a
    a={}
print(b)
