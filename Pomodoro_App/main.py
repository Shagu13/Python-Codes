import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# * by 60 as in 1 min there is 60 sec
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, 'bold'), fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, 'bold'), fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Note count_down function has to be called after Canvas has been created.
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60  # remainder 100/60 is 40, which is 01:40 secs
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)
        # ---------------------------- UI SETUP ------------------------------- #


# Note count_down function has to be called after Canvas has been created.
window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# to put the image in the middle, take half value of width and height as x and y value, also an image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(font=(FONT_NAME, 12, 'bold'), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 8, 'bold'), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, 'bold'), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
