# # Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}




# d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d2= {}
# for i,j in d1.items():
#    if j > 170:
#       d2[i] = j
# print(d2)


a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5]
print(dict(zip(a,b)))



# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# keys = list(num)
# print(keys[2])

# a = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# b = {'x': 300, 'y': 'Red', 'z': 600}

# d2 = {}
# for k,v in a.items():
#     d2.setdefault(k,[]).append(v)

# for i,j in b.items():
#     d2.setdefault(i,[]).append(j)

# print(d2)