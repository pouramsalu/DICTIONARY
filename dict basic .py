# dict={'name','bhavna','age','18'}
# x=dict.keys()
# print(x)

# # correct
# dict={'name':'salu','age':'20'}
# x=dict.items()
# print(x)


# correct
# dict={'name':'salu','age':8}
# x=dict.values()
# print(x)


# def function(num):
#     i=0
#     while i<num:
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")
#         i+=1
# num=int(input("enter the number:"))
# function(num)





# dict={'name':'salu','age':'19'}
# x=dict.pop('name')
# print(x)


# correct
# dict={1:2,2:3,4:6}
# del dict[2]
# print(dict)


# # correct
# dict={1:2,2:3,4:6}
# dict.copy()
# print(dict)


# # correct
# dict={1:2,2:3,4:6}
# dict.clear()
# print(dict)


# dict.update({5:7})
# print(dict)


# # correct
# dict={1:2,2:3,1:4,2:2}
# print(dict)


# dict={"name":"salu","age":"19","study":"coding"}
# x=dict.setdefault("n","s")
# print(x)

# Dictionary1 = { 'A': 'Geeks', 'B': 'For'}
 
# # using setdefault() method
# # when key is not in the Dictionary
# # Third_value = Dictionary1.setdefault('D')
# # print("Dictionary:", Dictionary1)
# # print("Third_value:", Third_value)
 

# Fourth_value = Dictionary1.setdefault('D', 'Good')
# # print("Dictionary:", Dictionary1)
# print("Fourth_value:", Fourth_value)



# Output: 

# Dictionary: {'A': 'Geeks', 'B': 'For', 'C': None}
# Third_value: None
# Dictionary: {'A': 'Geeks', 'B': 'For', 'C': None, 'D': 'Geeks'}
# Fourth_value: Geeks


# # correct
# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# for i in d:
#     print(i)


# correct
d={'a':1,'b':2,'c':3,'d':4,'e':5}
for i in d:
    print(d[i])

