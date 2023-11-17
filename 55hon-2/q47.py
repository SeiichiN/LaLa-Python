a = [5, 4, 3, 2, 1]
b = [n + a.index(n) for n in a]
print(b)
c = [i+n for i, n in enumerate(a)]
print(c)
