from itertools import permutations, product

words = set()
for word in permutations('kapkan', r=6):
    word = ''.join(word)
    if not ('aa' in word or 'kk' in word):
        words.add(word)
print(len(words))
