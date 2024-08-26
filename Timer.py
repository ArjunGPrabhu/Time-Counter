import time
from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Timer Counter")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable= hour)
hourEntry.place(x= 80, y= 20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable= minute)
minuteEntry.place(x= 130, y= 20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable= second)
secondEntry.place(x= 180, y= 20)

def countdown(temp):
    if temp > 0:
        mins, secs = divmod(temp, 60)
        hours = 0
        
        if mins >= 60:
            hours, mins = divmod(mins, 60)
            
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        second.set("{:02d}".format(secs))
        
        root.after(1000, countdown, temp - 1)
    else:
        # hour.set("00")
        # minute.set("00")
        # second.set("00")
        messagebox.showinfo("Time Countdown", "Time's Up!")

def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        countdown(temp)
    except ValueError:
        print("Please input the right value")
    
btn = Button(root, text= 'Set Time Countdown', bd= '5', command= submit)
btn.place(x= 70, y= 120)

root.mainloop()