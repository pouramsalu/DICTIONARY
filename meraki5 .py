# REMOVING ELEMENTS FROM A DICTIONAY
# POP():

# CAR_DETAILS={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)


# # POPITEMS()removes the last inserted list
# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# person.popitem()
# print(person)


# Using the del keyword we can remove a specified element from the dictionary.
dict={
'name':'jack',
'id':22,
'place':'dharamsala'
}
del dict('name')
print(dict)
