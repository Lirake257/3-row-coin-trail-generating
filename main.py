import random
import time
currow=1
lastrow=1
Run=True
totalrowcount=[0,0,0]
cd=0.05
currowcount=0
while Run:
    if currow==1:
        IsRowChange=random.randint(0,1)
        if IsRowChange==0 and currowcount>=1:
            currow=random.choice([0, 2])
            currowcount=0
        else:
            currowcount+=1
    else:
        IsRowChange=random.randint(0,3)
        if IsRowChange==0 and currowcount>=1:
            if currow==0:
                currow=1
            else:
                currow=1
            currowcount=0
        else:
            currowcount+=1
    
    restoprint=list(' ' * 4 * 3)
    restoprint[abs(currow*4+lastrow*4)//2]='*'
    restoprint = ''.join(restoprint)
    print('| ', restoprint[:-2], '|')
    time.sleep(cd)
    
    restoprint=list(' ' * 4 * 3)
    restoprint[currow*4]='*'
    restoprint = ''.join(restoprint)
    print('| ', restoprint[:-2], '|')
    totalrowcount[currow]+=1
    time.sleep(cd)
    lastrow=currow
