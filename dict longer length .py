# print the longer length in middle

a='123'
b='12'
c=[]
i=0
while i<len(a):
    if a>b:
        c=b+a+b
    else:
        c=a+b
    i+=1
print(c)