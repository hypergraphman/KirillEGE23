from itertools import permutations, product

words = set()
for word in product('skola', repeat=3):
    word = ''.join(word)
    if word.count('k') == 1:
        words.add(word)
print(len(words))
