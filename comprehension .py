# comprehension
# for i in range(1,int(input())):
#     print(i*10**i//9)

# for i in range(1,int(input())+1):
#     print(((10**i-1)//9)**2)


# a={x:x**2 for x in [1,2,3]}
# print(a)

a=["i love you","a little","alot","passionately","madly","not at all"]
i=0
b=" "
while i<len(a):
    if a[i]:
        b.append(a[i])
        i+=1
print(b)