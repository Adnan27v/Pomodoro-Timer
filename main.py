from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
# noinspection SpellCheckingInspection
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_clock_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check.config(text="",fg=GREEN)

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1

    if reps == 8:
        timer_label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_SEC)
        reps = 0
    elif reps%2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_SEC)

    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minute = count // 60
    seconds = count % 60

    if seconds <10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_clock_text, text=f"{minute}:{seconds}")
    if count > 0:
       global timer
       timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2 == 0:
            check.config(text="✔"*int(reps//2), fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_clock_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

#Start Button
start = Button(text="Start",command=start_timer)
start.grid(row=2,column=0)

#Reset Button
reset = Button(text="Reset",command=reset_timer)
reset.grid(row=2,column=2)

#Check-mark
check = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,12,"bold"))
check.grid(row=2,column=1)

#Timer text
timer_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

window.mainloop()