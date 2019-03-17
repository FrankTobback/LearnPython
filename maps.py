from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

#using for loop
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

#map function
#map(function, data)
#print(list(map(jumble,words)))

#comprehension way
print([jumble(word) for word in words])
