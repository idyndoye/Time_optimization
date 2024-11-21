import math
from cgitb import reset
from operator import countOf
from tkinter import *
from math import *
from urllib.response import addinfo

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1

    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_second)
        Title_label.config(text="Break", fg=RED)
    if reps % 2 == 0:
        Title_label.config(text="Break", fg=PINK)
        count_down(short_break_second)
    else:
        count_down(work_second)
        Title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        window.after(1000,count_down, count - 1)
    else:
        start_time()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("time optimization")
window.config(padx=100, pady=50, bg=YELLOW)


Title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
Title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#creating the start and rest button
start_button = Button(text="start",highlightthickness=0, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

#adding the check mark
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)



window.mainloop()
