'''
convert time in 12hr format
 time=21:59:60

 9:10:0
 '''
time='24:60:60'
time=time.split(":")
hrs=time[0]
min=time[1]
sec=time[2]
if int(hrs)>=24:
    hrs=int(hrs)-12
if int(min)>59:
    hrs=int(hrs)+1
    min=int(min)-60
if int(sec)>59:
    min=int(hrs)+1
    sec=int(sec)-60
print(str(hrs)+':'+str(min)+':'+str(sec))
    

