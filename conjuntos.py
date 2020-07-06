lista = [1,2,3,4,4,5]
s = set(lista)
s
print(s)

s1 = {1,2,3,6}
s2 = {3,4,5,6}
s1.union(s2)
print(s1)

s1 = {1,2,3,6}
s2 = {3,4,5,6}
s1.intersection(s2)
print(s1)

s1 = {1,2,3,6}
s2 = {3,4,5,6}
s1.differnce(s2)
print(s1)