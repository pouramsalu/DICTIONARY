# **returns the value of the specified keys

# dict={"A":1,"B":2}
# print(dict.get("A"))
# print(dict.get("C"))
# print(dict.get("C,not found!"))

# DICTIONARY GET() METHOD NESTED
test_dict={"abc":{'is':'best'}}
print('the original dictionary is:'+str(test_dict))
res=test_dict.get("abc",{}.get('is'))
print("the nested safely accessed value is:"+str(res))
