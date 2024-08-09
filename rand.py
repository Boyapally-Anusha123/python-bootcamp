import random
ran=random.randint(1,10) 
chance=3
while chance>=1:
    guess=int(input())
    if guess==ran:
        print('congrats')
        break
    else:
        chance-=1
        continue
if chance<1:
    print('failed better luck next time')

 
