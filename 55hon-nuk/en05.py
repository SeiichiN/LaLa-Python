list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
s1 = set1 & set2
s2 = set1 | set2
print(s1)
print(s2)

j = len(s1)/len(s2)
print(j)
