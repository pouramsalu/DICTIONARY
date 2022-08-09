# # returns a dictionary with the specified keysand value

# # demonstrating the working of fromkeys
# seq={'a','b','c','d','e'}
# res_dict=dict.fromkeys(seq)
# print("the newly created dict with none values:"+str(res_dict))
# res_dict=dict.fromkeys(seq,1)
# print('the newly created dict with 1 as value:'+str(res_dict))


# keys={"a","e","i","o","u"}
# vowels=dict.fromkeys(keys)
# print(vowels)

# keys={"a","e","i","o","u"}
# value=[1]
# vowels=dict.fromkeys(keys,value)
# print(vowels)
# value.append(2)
# print(vowels)

# seq={"a","b","c","d","e"}
# list1=[2,3]
# res_dict=dict.fromkeys(seq,list1)
# print("the newly created dict with list value:"+str(res_dict))
# list1.append(4)
# print("the dict with list value after appending:"+str(res_dict))
# list1=[2,3]
# print('\n')
# res_dict2={"keys:list(list1) for key in seq"}
# print("the newly created dict with list values:"+str(res_dict))
# list1.append(4)
# print("the dict with list values after appending(no change):"+str(res_dict2))


# x=('keys1','keys2','keys3')
# y=0
# d=dict.fromkeys(x,y)
# print(d)

# # *dictionary fromkeys()with an empty list
# new_dict=dict.fromkeys(range(4),(1))
# print("new dictionary with empty lists as keys:"+str(new_dict))


# # vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]
# vowels = { key : list(value) for key in keys }
# # you can also use { key : value[:] for key in keys }
# print(vowels)
# # updating the value
# value.append(2)
# print(vowels)

dict={1,2,3}
a=dict.fromkeys(",salu")