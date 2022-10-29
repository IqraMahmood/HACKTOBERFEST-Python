#Dictionary is mutable unordered collection with elements in form of key:value pair that associate key to value.

dic = {1:'a',2:'b',3:'c',4:'d',5:'e'}

print(dic[4])  #d

dic[3]='f'
print(dic[3])  #f


# Merge two dictionaries

d1 = {'a': 1, 'b': 2, 'c': {'d': 3}}
d2 = {'b': 4, 'c': {'d': 5, 'e': 6}}

merged = {**d1, **d2}
print(merged) # {'a': 1, 'b': 4, 'c': {'d': 5, 'e': 6}}
