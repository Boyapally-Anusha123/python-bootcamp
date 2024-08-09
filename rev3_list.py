arr=[1,2,3,4,5]
k=4
#5,4,1,2,3
first=arr[k+1:k-(k-2):-1]
second=arr[:k-1]
print(first+second)
