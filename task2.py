'''
s='abc'
k=2
f=s[:len(s)//k+1]
a=s[len(s)//k:]
b=s[:len(s)//k]
print(f,a,b)
'''
import itertools
s = 'abc'
k = 2
combinations = list(itertools.combinations(s, k))
for combo in combinations:
    print(''.join(combo))


