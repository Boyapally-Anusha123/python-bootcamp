def check(s):
    s=s.split()
    s=list(reversed(s)) # s became revers list
    print(s)
    for i in s:
        rev=i[::-1] #characters of reverse list
        print(rev,end='')
s='sri devi is engineering college'
check(s)
