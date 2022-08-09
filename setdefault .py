# setdefault: returns the values of the specified keys.if the keys doesn't exist,insert
# the keys with the specified values

# person = {'name': 'Phill', 'age': 22}
# age = person.setdefault('age')
# print('person = ',person)
# print('Age = ',age)


person = {'name': 'Phill'}
# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)
# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)