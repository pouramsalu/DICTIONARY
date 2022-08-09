# # return a copy of the dictionary
# a={1:'salu',2:'coding'}
# new=a.copy()
# print(new)


# a={1:'salu',2:'coding'}
# new=a.copy()
# print('new:',new)
# print('a:',a)

# correct
dict={1:2,2:3,4:6}
dict.copy()
print(dict)



# # # copy()and update
# dict1={10:'a',20:[1,2,3],30:'c'}
# print('given dictionary:',dict1)
# dict2=dict1.copy()
# print('new copy:',dict2)
# dict2[10]=10
# dict2[20][2]='45'
# print('updated copy:',dict2) 


# # how is it different from simple assingning"="?
# a={1:'salu',2:'coding'}
# new=a.copy()
# new.clear()
# print('new:',new)
# print('a:',a)
# a={1:'one',2:'two'}
# new=a
# new.clear()
# print('new:',a)
# print('a:',a)
