doc = 'i bought an apple .\ni ate it .\nit is delicious .'
lst = doc.replace('\n', ' ').split(' ')
print(lst)
word2freq = {}
for k in lst:
    if k in word2freq:
        word2freq[k] += 1
    else:
        word2freq[k] = 1

print(word2freq)
