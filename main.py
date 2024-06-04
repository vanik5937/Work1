from tkinter import *
from math import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = NONE

def timer_reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0
    marks = ""
    checkmark.config(text=marks)


def start_timer():
    global reps
    reps += 1

    ws = WORK_MIN * 60
    sb = SHORT_BREAK_MIN * 60
    lb = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        countdown(lb)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(sb)
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(ws)

def countdown(count):
    count_min = floor(count/60)
    count_sec = count%60
    if count_sec<10:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>=0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()

        marks = ""
        worksession = floor(reps/2)

        for _ in range(worksession):
            marks = marks + "✔"
        checkmark.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(height=224, width=200, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


timer_label = Label(text="Timer", fg="black", bg = YELLOW, font=(FONT_NAME,50))
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0, command=timer_reset)
reset_button.grid(row=2,column=2)

checkmark = Label(bg = YELLOW,fg=GREEN, font= (FONT_NAME,17,"bold"), highlightthickness=0)
checkmark.grid(row=2,column=1)
window.mainloop()