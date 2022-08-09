# Q14.Write a Python program to multiply all the items in a dictionary.

dict={'a':4,'b':7,'c':6,'d':9}
def salu(dict):
    mul=1
    for i in dict:
        mul=mul*dict[i]
    return mul
print(salu(dict))


