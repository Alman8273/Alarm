#Alarm Clock with GUI 
from tkinter import *
import datetime
import time
from tkinter import font
import winsound

#Loop
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

#GUI with tkinter
clock = Tk()
clock.resizable(0,0)
clock.title("Alarm Clock")
clock.geometry("300x150")
time_format = Label(clock, text= "Enter time in 24 hour format!", fg="black",bg="cyan",font="Arial 14 bold",).place(x=20,y=85)
addTime = Label(clock,text = " Hr   Min  Sec ",font=60).place(x = 80)

#alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=80,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 14).place(x=115,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 7).place(x=165,y=30)

#Input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x=215,y=25)

clock.mainloop()


