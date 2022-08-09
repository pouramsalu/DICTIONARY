# Q31.. Write a Python program to get the top three items in a shop. 
dict= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 
'item4':55, 'item5': 24}
x=0
y=0
z=0
for i in dict:
    for j in dict:
        if dict[j]>x:
            x=dict[j]
            a=j
        elif dict[j]>y and dict[j]<x:
            y=dict[j]
            b=j
        elif dict[j]>z and dict[j]<y:
            z=dict[j]
            c=i
print(a,x)
print(b,y)
print(c,z)