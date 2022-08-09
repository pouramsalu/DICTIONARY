
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
e = {}
for v in reversed(sorted(d.values())):
    for k in d:
        if d[k] == v and k not in e:
            e.update({k:v})
print(e)