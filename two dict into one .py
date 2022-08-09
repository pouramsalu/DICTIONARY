# # Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# for i in dict1:
#     for i in dict2:
#         continue
# dict1.update(dict2)
# print(dict1)


dict1={'salu':20,'riamroi':12}
dict2={'vinod':25,'rahul':27}
for i in dict1:
    for i in dict2:
        continue
dict1.update(dict2)
print(dict1)
