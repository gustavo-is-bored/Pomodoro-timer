import time as tm
import math
import winsound

run = False
delt = 0
valid = False
noise = False
pomodoro = [50*60, 10*60, 25*60]
sessions = ["Work session", "Short break", "Long break"]
freq1 = 840
freq2 = 560
duration = 900
blip = math.trunc(duration/2)

def insound():
    winsound.Beep(freq1, duration)
    winsound.Beep(freq1, blip)
    winsound.Beep(freq2, duration)

def outsound():
    winsound.Beep(freq2, duration+50)
    winsound.Beep(freq1, duration+200)

def session(time):
    t1 = tm.time()
    insound()
    while True:
        delt = round(tm.time() - t1)
        session = (delt % (pomodoro[0]+pomodoro[1]+2))
        if session <= time:
                    work = time - session
                    seconds = work % 60
                    minutes = math.trunc(work/60)
                    if work == 1 and noise == False: 
                        outsound()
                        noise = True
                    if work == 2:
                        noise = False
        else:
             break

while True:
    init = input("Hello! Are you ready to start? (y/n): ")
    if init == "y":
        while valid == False:
            custo = input("Enter 1 to use default sessions, or 2 to customise: ")

            if custo == "1" or custo == "2":
                valid = True
            else:
                print("Invalid input. Please enter 1 or 2.")

            if custo == "2":
                for i in range(3):
                    while True: 
                        n = input(sessions[i] + " in minutes: ")

                        try:
                            int(n)
                        except ValueError:
                            print("Invalid input. Please input an integer number.")
                        else:
                            pomodoro[i] = int(n)*60
                            break
                print("Okay, preferences saved.")
            if custo == "1":
                print("Got it. Short breaks will automatically begin after work sessions.")
            if valid == True:
                valid = False
                while valid == False:
                    auto = input("Would you like to automate sessions? (y/n): ")
                    if auto == "y" or auto == "n":
                        valid = True
                    else:
                        print("Invalid input. Please enter 1 or 2.")
                                      
                    if auto == "y":
                        print("Got it. A short break will automatically begin after each work session")
                        tm.sleep(1)
                        while True:
                            print("Starting work session! (" + str(math.trunc(pomodoro[0]/60)) + " minutes)")
                            session(pomodoro[0])
                            print("Starting short break! (" + str(math.trunc(pomodoro[1]/60)) + " minutes)")
                            session(pomodoro[1])
                    if auto == "n":
                        print("Got it. I'll check before we begin sessions, and you'll have the chance to choose a longer break, or dive right into another work session")
                        tm.sleep(1)
                        print("Starting work session! (" + str(math.trunc(pomodoro[0]/60)) + " minutes)")
                        session(pomodoro[0])
                        valid = True
                        while valid == True:
                            n = input("Enter 1 for a work session, 2 for a short break, 3 for a long break, or 4 to automate: ")

                            if n == "1":
                                print("Starting work session! (" + str(math.trunc(pomodoro[0]/60)) + " minutes)")
                                session(pomodoro[0])
                            elif n == "2":
                                print("Starting short break! (" + str(math.trunc(pomodoro[1]/60)) + " minutes)")
                                session(pomodoro[1])
                            elif n == "3":
                                print("Starting long break! (" + str(math.trunc(pomodoro[2]/60)) + " minutes)")
                                session(pomodoro[2])
                            elif n == "4":
                                valid = False
                            else:
                                print("Invalid input. Please choose 1, 2, 3, or 4.")
    if init == "n":
        print("Goodbye!") 
        break
    else: print("Invalid input. Please enter y or n.")
