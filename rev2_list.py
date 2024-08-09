arr=[1,2,3,4,5]
k=3
#[5,4,3,1,2]
first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)
