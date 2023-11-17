doc = 'i bought an apple .\ni ate it .\nit is delicious .'
_lst = doc.split('\n')
new_list = []
for line in _lst:
    lst = line.split(' ')
    new_list += lst
print(new_list)

word2freq = {}
for k in new_list:
    if k in word2freq:
        word2freq[k] += 1
    else:
        word2freq[k] = 1

print(word2freq)
