# Write a program to print 'exists' if entered key already exists in the dictionary and print'
# not exists' if the entered key does not exist.

dict1={"name":"Raju", "marks":56}
n=input("enter the str:")
for i in dict1:
    if i==n:
        print('exist')
        break
    else:
        print("not exist")
        break