a = [5, 4, 3, 2, 1]
c = [a.index(n) for n in a]
b = [n+a.index(n) for n in a]
print(c)
print(b)

d = [i+name for i, name in enumerate(a)]
print(d)
