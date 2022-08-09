# Write a Python program to split a given dictionary of lists into list of dictionaries.

d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
x=[]
a,b=d.values()
for i in range(len(a)):
    for j,k in d.items():
        b=({j:k[i]})
        x.append(b)
print(x)

