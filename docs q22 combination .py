# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
dict={'1':['a','b'], '2':['c','d']}
a,b=dict.values()
for i in a:
    for j in b:
        print(i+j)



