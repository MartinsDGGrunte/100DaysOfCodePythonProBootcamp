from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# instance of a window
window = Tk()
# set title
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

# instance of Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# instance of image
tomato_image = PhotoImage(file="../media/tomato.png")
# create image
canvas.create_image(100, 112, image=tomato_image)
# create text
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# add text to canvas
canvas.grid(column=1, row=1)

# create title label
title_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# create start button
start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

# create reset button
start_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(column=2, row=2)

# create check label
check_label = Label(text="", font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# main loop of window
window.mainloop()
