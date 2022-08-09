# # popitems:removes the last inserted key value pair
# person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# # ('salary', 3500.0) is inserted at the last, so it is removed.
# result = person.popitem()
# print('Return Value = ', result)
# print('person = ', person)
# # inserting a new element pair
# person['profession'] = 'Plumber'
# # now ('profession', 'Plumber') is the latest element
# result = person.popitem()
# print('Return Value = ', result)
# print('person = ', person)


a={1:2,2:3,3:4,7:9}
a.popitems()
print(a)