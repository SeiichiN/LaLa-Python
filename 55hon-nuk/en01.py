count = 0
lst1 = list(range(1, 32))
lst2 = list(range(1, 13))
print(lst1)
print(lst2)
for n1 in lst1:
    for n2 in lst2:
        if n1 % 10 == n2 % 10:
            print(f'n1:{n1} n2:{n2}')
            count += 1
print(count)
