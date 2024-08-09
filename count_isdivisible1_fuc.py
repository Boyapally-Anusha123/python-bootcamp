def check(arr):
    c=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end='')
            c+=1
    return c
arr=list(map(int,input().split()))
print(check(arr))
