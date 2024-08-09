s=7 #starting of sams house
t=11 #ending of sams house
a=3  #apple tree position
b=15 #orange tree position
apples=[6,5,-4]
oranges=[9,8,-4]
a1,b1=0,0
for i in apples:
    if a+i>=s:   #a+i in range(s,t+1)
        a1+=1
for i in oranges:
    if b+i<=t:    #b+i in range(s,t+1)
        b1+=1
print(a1,b1)
