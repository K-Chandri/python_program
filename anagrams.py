from collections import Counter
a = 'lost'
b = 'tosl'
print(Counter(a)==Counter(b))


a = 'lost'
b = 'stl'
if sorted(a)==sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")