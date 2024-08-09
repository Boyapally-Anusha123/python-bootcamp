'''
remove duplicate words
o/p:
hello world good moring afternoon
'''
s='hello world hello world good moring good afternoon'
s=s.split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s1=' '
for k,v in d.items():
    if v>=1:
        s1+=k+' '
print(s1)
