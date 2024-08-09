arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
  if key not in d:
    d[key]=1
  else:
    d[key]+=1
print(d)
