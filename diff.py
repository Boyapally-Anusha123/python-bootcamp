
'''
find sum min of all digits
find sum max of all digits
print differnce b/w min and max

without funcs:
n1=7823
n2=5489
n3=1384
n1=str(n1)
n2=str(n2)
n3=str(n3)
a=min(n1)
b=min(n2)
c=min(n3)
m=int(a)+int(b)+int(c)
a1=max(n1)
b1=max(n2)
c1=max(n3)
m1=int(a1)+int(b1)+int(c1)
diff=abs(m-m1)
print(diff)

'''
n1=7823
n2=5489
n3=1384
smin=0
smax=0
def min_check(n):
    s=str(n)
    min=int(s[0])
    for i in s:
        if int(i)<min:
            min=int(i)
    return min
def max_check(n):
    s=str(n)
    max=int(s[0])
    for i in s:
        if int(i)>max:
            max=int(i)
    return max
smin=min_check(n1)+min_check(n2)+min_check(n3)
smax=max_check(n1)+max_check(n2)+max_check(n3)
diff=abs(smin-smax)
print(diff)

    



























    



