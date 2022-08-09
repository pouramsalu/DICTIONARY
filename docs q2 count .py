# write a python program to create a dictionary from a string
# sample: w3resource


sample="w3resource"
i=0
a={}
while i<len(sample):
    j=0
    count=0
    while j<len(sample):
        if sample[i]==sample[j]:
            count+=1
        j+=1
    a.update({sample[i]:count})
    i+=1
print(a)
