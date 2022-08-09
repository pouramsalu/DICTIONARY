# update the dictionary with the specified key-values pair


# marks = {'Physics':67, 'Maths':87}
# internal_marks = {'Practical':48}

# marks.update(internal_marks)
# print(marks)


# dictionary = {'x': 2}
# dictionary.update([('y', 3), ('z', 0)])
# print(dictionary)


d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print(d)
d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print(d)