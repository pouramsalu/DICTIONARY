a=['4327']
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        c=int(a[i][j])*int(a[i][j])
        print(c)
        j+=1
    i+=1

# dict={'key1':'salu','key2':'riamroi'}
# for i in dict:
#     c=dict[i]
#     print(c)
