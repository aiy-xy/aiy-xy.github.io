#myClock ext stop or infinity.py
from datetime import datetime

while True:
    print ()
    print ('Computer races: which is the fastest?')
    print ('option stop or infinity?')
    soi = input()
    if soi == 'infinity':
        while True:
            now = datetime.now()
            month = str(now.month)
            day = str(now.day)
            year = str(now.year)
            hour = str(now.hour)
            minutes = str(now.minute)
            seconds = str(now.second)

            rightnow = str (year + month + day+ hour + minutes + seconds)
            print (now)

    elif soi =='stop':
        print ('how many times?')
        times = int(input())

        for guessesTaken in range(1, times):
            now = datetime.now()
            month = str(now.month)
            day = str(now.day)
            year = str(now.year)
            hour = str(now.hour)
            minutes = str(now.minute)
            seconds = str(now.second)

            rightnow = str (year + month + day+ hour + minutes + seconds)
            print (now)

    else:
        print('try again')
            

