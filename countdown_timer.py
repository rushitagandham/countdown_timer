import time
import keyboard
import os

timer = 0

def resume():  #this functions returns to countdown function and continues the timer from where it left off
    print("Press and hold 1 to pause")
    print("Press and hold 2 to stop")
    print("Resuming the timer...")
    return
    
def reset(): #this function resets the timer to the value the user initially entered
    print("Press and hold 1 to pause")
    print("Press and hold 2 to stop")
    print("Resetting the timer...")
    countdown(timer) #calls the countdown function with initial value as parameter
    
def restart(): #this function goes back to start function where user can set new value for the timer
    print("Press and hold 1 to pause")
    print("Press and hold 2 to stop")
    print("Restarting the timer...")
    start() #calls start
    
def stop(t): #stops the timer
    os.system("cls")
    print_timer(t) 
    print("Timer Stopped")
    print("timer = "+print_timer(t))
    print("Press 1 to reset")
    print("Press 2 to restart")
    print("press 3 to exit")
    op = int(input())
    os.system("cls")
    if(op==1):
        reset()
    if(op==2):
        restart()
    if(op==3):
        print("Exiting...")
        exit()
        
    
def pause(t): #pauses the timer
    os.system("cls")
    print("Timer Paused")
    print("timer = "+print_timer(t))
    print("Press 2 to resume")
    print("Press 3 to reset")
    print("Press 4 to restart")
    s = int(input("Enter option: "))
    os.system("cls")
    if(s==2):
        resume()
    if(s==3):
        reset()
    if(s==4):
        restart()
        
def print_timer(t): #return the current value of the timer
    mins,secs = divmod(t,60) 
    timer = '{:02d}:{:02d}'.format(mins,secs) #used to format the timer
    return timer
    
def countdown(t): #decrements and prints the timer and checks for user input for pause/stop
    while t:
        while True:
            if keyboard.is_pressed("1"): #checks if '1' key is pressed by the user
                pause(t)  #calls the pause func with current value of timer as parameter
                break
            elif keyboard.is_pressed("2"): #checks if '2' key is pressed by the user
                stop(t) #calls the stop func with current value of timer as parameter
                break
            else:
                print(print_timer(t),end = "\r") #prints the timer on terminal
                time.sleep(1) #stops exxecution for 1 second
                break
    
        t = t - 1 #decrements timer
    print("Timer completed!!") #prints when timer reaches 0
    time.sleep(1)
    start()

def start(): #takes the value for the timer from user in seconds
    global timer
    os.system("cls")
    print("\n\n------------------------COUNTDOWN TIMER------------------------")
    timer = int(input("Enter time in seconds for the timer to run: "))
    print("PRESS and HOlD 1 to pause")
    print("PRESS and HOLD 2 to stop")
    print("Timer is starting....")
    countdown(timer)    #calls countdown function

if __name__ == "__main__":        #execution starts from here
    start()         #start function gets called
    