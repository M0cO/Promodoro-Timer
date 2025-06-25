from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(start_time, text="00:00")
    timer_label.config(text="Work")
    checkmark.config(text="")
    global reps
    reps = 0

def timer_started():
    global reps
    reps += 1
    work_sessions = math.floor(reps / 2)
    marks = "✓" * work_sessions
    checkmark.config(text=marks)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN, 0)
        timer_label.config(text="Long Break", fg=YELLOW, bg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN, 0)
        timer_label.config(text="Break", fg=GREEN)
    else:
        count_down(WORK_MIN, 0)
        timer_label.config(text="Work", fg=RED)

def count_down(min, sec):
    canvas.itemconfig(start_time, text=f"{min:02d}:{sec:02d}")
    if sec > 0:
        global timer
        timer = window.after(1000, count_down, min, sec - 1)
    else:
        if min > 0:
            window.after(1000, count_down, min - 1, 59)
    if canvas.itemcget(start_time, "text") == "00:00":
        timer_started()

window = Tk()
window.title("Promodoro Timer")
window.config(padx=100, pady=50, bg=PINK)

timer_label = Label(window, text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 35))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
img = PhotoImage(file="tomato.png") #image upload 1/2
canvas.create_image(100, 112, image=img) #image upload 2/2
start_time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

checkmark = Label(window,text="", bg=PINK, fg=GREEN, font=(FONT_NAME, 26, "bold"))
checkmark.grid(row=3, column=1)

start_button = Button(window, text="Start", command=timer_started, highlightbackground=PINK)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", command=reset_timer, highlightbackground=PINK)
reset_button.grid(row=2, column=2)

window.mainloop()
