doc = 'i bought an apple .\ni ate it .\nit is delicious .'
_lst = doc.split('\n')
word2freq = {}
for line in _lst:
    lst = line.split(' ')
    for word in lst:
        word2freq[word] = word2freq.get(word, 0) + 1
        
print(word2freq)
