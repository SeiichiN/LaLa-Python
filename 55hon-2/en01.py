list1 = list(range(1, 32))
list2 = list(range(1, 13))
print(list1)
print(list2)
count = 0
for n1 in list1:
    for n2 in list2:
        if n1 % 10 == n2 % 10:
            count += 1
            # print(n1, n2)
print(count)
