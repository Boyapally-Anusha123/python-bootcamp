cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
 }
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
 }
s=0
s1=0
for k,count in cong.items():
    if k>=18:
        s+=count
for k,count1 in bjp.items():
    if k>=18:
        s1+=count1
diff=abs(s-s1)
if s>s1:
    print('cong',diff)
else:
    print('bjp',diff)
