list1 = [12, 23, 34, 45, 56, 67, 78, 89]
list2 = [21, 32, 43, 45, 65, 67, 78, 98]
set1 = set(list1)
set2 = set(list2)
print(set1)    # {34, 67, 12, 45, 78, 23, 56, 89}
print(set2)    # {32, 65, 98, 67, 43, 45, 78, 21}
seki = set1 & set2
wa = set1 | set2
print(seki)    # {67, 45, 78}
print(wa)      # {32, 65, 34, 67, 98, 43, 12, 45, 78, 21, 23, 56, 89}
jaccard = len(seki) / len(wa)
print(jaccard)   # 0.23076923076923078

