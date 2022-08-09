# dict={'a':20,'b':42,'c':34}
# max=0
# for i in dict:
#     if dict[i]>max:
#         max=dict[i]
#         # max_key=i
# print(max)
# print(max_key)

# # Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# # Original Dictionary:
dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# # 1 maximum value(s) in the said dictionary:
# # ['f']
# # 2 maximum value(s) in the said dictionary:
# # ['f', 'i']
# # 5 maximum value(s) in the said dictionary:
# # ['f', 'i', 'g', 'd', 'c']
max=0
sec=0
third=0
d=[]
for i in dic:
    for j in dic:
        if dic[i]>max:
            max=dic[j]
            a=j
        # elif dic[j]>sec and dic[j]<max:
        #     sec=dic[j]
        #     b=j
        # elif dic[j]>third and dic[j]<sec:
        #     third=dic[j]
        #     c=j
d.append(a)
# d.append(b)
# d.append(c)
print(d)

