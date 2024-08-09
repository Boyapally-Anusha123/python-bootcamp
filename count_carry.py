n1=288
n2=594
'''
count the no.of carry?
'''
count=0
carry=0
while n1>0 and n2>0:
    rem1=n1%10
    rem2=n2%10
    sum=carry+rem1+rem2
    if (sum>9):
        carry=1
        count+=1
    else:
        carry=0
    n1=n1//10
    n2=n2//10
print(count)
