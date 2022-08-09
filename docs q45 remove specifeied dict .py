# Write a Python program to remove a specified dictionary from a given list. 

list=[{'id': 'FF0000', 'color': 'Red'}, {'id': '800000', 'color': 'Maroon'}, {'id': 'FFFF00', 'color': 'Yellow'}, {'id': '808000', 'color': 'Olive'}]

pop='FF0000'
a=[]
for i in list:
    if pop in i.values():
        pass
    else:
        a.append(i)
print(a)