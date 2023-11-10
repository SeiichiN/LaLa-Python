a = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}

lst = []
for k in a.keys():
    lst.append(k)
print(lst)

lst = [k for k in a.keys()]
print(lst)
    
