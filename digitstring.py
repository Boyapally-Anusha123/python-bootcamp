s='a1b2c3d492nm45'
'''
output:
    12349245abcdnm
'''
first=''
second=''
for i in s:
    if i.isdigit():
        first+=i
    else:
        second+=i
print(first+second)
