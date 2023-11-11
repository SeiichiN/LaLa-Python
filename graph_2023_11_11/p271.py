
f = open('readme.txt', 'r', encoding='UTF-8')
lines = [n.rstrip('\n') for n in f.readlines()]

print(lines)

f.close()