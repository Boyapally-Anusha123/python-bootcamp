
'''
remove duplicate words
o/p:
hello world good moring afternoon
'''
s='hello world hello world good moring good afternoon'
s1=''
s=s.split()
for i in s:
    if i not in s1:
        s1=s1+i+' '
print(s1)
