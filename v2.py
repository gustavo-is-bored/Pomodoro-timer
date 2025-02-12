import time as tm
import math
import winsound

run = False
t = 0
delt = 0
pshort = False
plong = False
noise = False
pomodoro = [5, 5, 5]  #  [50*60, 10*60, 25*60]
n = 0
session = 0
long = 0
short = 0
freq1 = 840
freq2 = 560
duration = 900
blip = math.trunc(duration/2)

def start():
    global run, t1
    print("Starting work session! (" + str(math.trunc(pomodoro[0]/60)) + " minutes)")
    worksound()
    run = True
    t1 = tm.time()

def shortbreak():
    global t2, pshort
    print("Starting short break!")
    pshort = True
    t2 = tm.time()

def longbreak():
    global t2, plong
    print("Starting long break!")
    plong = True
    t2 = tm.time()

def worksound():
    winsound.Beep(freq1, duration)
    winsound.Beep(freq1, blip)
    winsound.Beep(freq2, duration)

def breaksound():
    winsound.Beep(freq2, duration+50)
    winsound.Beep(freq1, duration+200)



while True:
    
    
    init = input("Are you ready to begin? (y/n): ")
    if init == "y" or init == "Y" or init == "yes" or init == "Yes" or init == "YES":
        start()
    elif init == "n" or init == "N":
        print("Wow. Okay. Fuck you too then.")
        break
    else:
        print("Invalid input. How did you manage to fuck this up?")
    
    while run == True:
        delt = round(tm.time() - t1)
        n = math.trunc((delt+pomodoro[1]+1)/(pomodoro[0]+pomodoro[1]+2))
        session = (delt % (pomodoro[0]+pomodoro[1]+2))

        while plong == True:
            long = pomodoro[2] - round(tm.time() - t2)
            seconds = long % 60
            minutes = math.trunc(long/60)

            if long+1 <= 0:
                plong = False
                t1 = t1 + pomodoro[2]
            if long == 2:
                noise = False
            if long == 1 and noise == False:
                winsound.Beep(freq1, duration)
                winsound.Beep(freq2, duration)
                #wazzy.play()
                noise = True

        while pshort == True:
            short = pomodoro[1] - round(tm.time() - t2)
            seconds = short % 60
            minutes = math.trunc(short/60)
            if short+1 <= 0:
                pshort = False
                t1 = t1 + pomodoro[1]
            if short == 2:
                noise = False
            if short == 1 and noise == False:
                winsound.Beep(freq1, duration)
                winsound.Beep(freq2, duration)
                #wazzy.play()
                noise = True

        if session <= pomodoro[0]:
            work = pomodoro[0] - session
            seconds = work % 60
            minutes = math.trunc(work/60)
            if work == 1 and noise == False: 
                print("Work done - short break (" + str(math.trunc(pomodoro[1]/60)) + " minutes)")
                breaksound()
                noise = True
            if work == 2:
                noise = False
            
        if pomodoro[1]+pomodoro[0]+1 >= session > pomodoro[0]:
            short = round(pomodoro[1]+1 - (session - pomodoro[0]))
            seconds = short % 60
            minutes = math.trunc(short/60)
            if short == 1 and noise == False:
                print("Back to work! (" + str(math.trunc(pomodoro[0]/60)) + " minutes)")
                worksound()
                noise = True
            if short == 2:
                noise = False