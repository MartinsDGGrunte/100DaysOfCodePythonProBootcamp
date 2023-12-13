from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 1
timer = None
start_active = FALSE


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    start_button.config(state="active")
    check_label["text"] = ""
    title_label["text"] = "Focus"
    title_label["fg"] = GREEN
    window.after_cancel(timer)
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start_button.config(state="disabled")
    if reps % 8 == 0:
        count_down(int(LONG_BREAK_MIN*60))
        title_label["text"] = "Long Break"
        title_label["fg"] = RED
        check_label["text"] += "✔"
    elif reps % 2 == 0:
        count_down(int(SHORT_BREAK_MIN*60))
        title_label["text"] = "Short Break"
        title_label["fg"] = PINK
        check_label["text"] += "✔"
    else:
        count_down(int(WORK_MIN*60))
        title_label["text"] = "Focus"
        title_label["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    whole_minutes = int(count / 60)
    seconds = count - (whole_minutes * 60)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    if whole_minutes < 10:
        whole_minutes = "0" + str(whole_minutes)
    else:
        whole_minutes = str(whole_minutes)

    if count > 0:
        if count == 1500:
            canvas.itemconfig(canvas_text, text="25:00")
            window.after(1000, count_down, count - 1)
        elif count < 1500:
            canvas.itemconfig(canvas_text, text=whole_minutes + ":" + seconds)
            global timer
            timer = window.after(1000, count_down, count - 1)

    if count == 0:
        canvas.itemconfig(canvas_text, text="00:00")
        global reps
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# instance of a window
window = Tk()
# set title
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

# instance of Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# instance of image
tomato_image = PhotoImage(file="media/tomato.png")
# create image
canvas_image = canvas.create_image(100, 112, image=tomato_image)
# create text
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# add text to canvas
canvas.grid(column=1, row=1)

# create title label
title_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# create start button
start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# create reset button
reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# create check label
check_label = Label(text="", font=(FONT_NAME, 22), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# main loop of window
window.mainloop()
