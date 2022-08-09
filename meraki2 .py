# # We can access dictionary values with the use of square brackets. 
# # Look at the example below to understand.MERAKI Q1
person={
'name':'jack',
'age':20,
'gender':'male',
4:'organisation'}
result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result)


# # We can also make use of the get() function to access dictionary 
# # values.
# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:{
# 'organisation':'navgurukul','place':'dharamsala'
# }
# }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)