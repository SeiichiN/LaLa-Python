doc = 'i bought an apple .\ni ate it .\nit is delicious .'
lst = doc.replace('\n', ' ').split(' ')
print(lst)
# ['i', 'bought', 'an', 'apple', '.', 'i', 'ate', 'it', '.', 'it', 'is', 'delicious', '.']
word2freq = {}
for w in lst:
    if w in word2freq:
        word2freq[w] += 1
    else:
        word2freq[w] = 1
print(word2freq)
# {'i': 2, 'bought': 1, 'an': 1, 'apple': 1, '.': 3, 'ate': 1, 'it': 2, 'is': 1, 'delicious': 1}
