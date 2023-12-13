'''s1 = {1,2,3,4}
s2 = {4,5,6,1}

print(s1.union(s2))
print(s1.difference(s2))
'''
#FrozenSet

s1 = {1,2,3,4,8,5,1,2}
fs1 = frozenset(s1)
fs2 = frozenset({3,4,5,6,7,1,2})

print(fs1.union(fs2))
print(fs1.difference(fs2))
print(fs2.difference(fs1))
