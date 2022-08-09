# Count the total number of items from the values of the dictionary which are in the form of a list.

# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#     for j in dict1[i]:
#         count+=1
# print(count)

# Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
for i in student:
    for j in student[i]:
        count+=1
print(count)