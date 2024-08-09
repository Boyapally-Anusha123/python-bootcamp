n=2397
m=3
'''
o/p:
592721
  if even digit then add with m
  if odd digit then multiply with m
'''
n=str(n)
for i in n:
     if int(i)%2==0:
        print(int(i)+m)
     else:
        print(int(i)*m)
    
       
