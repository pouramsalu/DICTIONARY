# **return a list containing the dictionary's keys
# dictionary1={"A":"Geeks","B":4,"C":"geeks"}
# print("dictionary items:")
# print(dictionary1.items())

# # correct
# dict={'name':'salu','age':'20'}
# x=dict.items()
# print(x)


#** to show working of items()after modification of dictionary
dictionary1={'A':'Geeks','B':4,'C':'Geeks'}
print('original dictionary items:')
print('items')
del[dictionary1['C']]
print('updated dictionary:')
print('items')